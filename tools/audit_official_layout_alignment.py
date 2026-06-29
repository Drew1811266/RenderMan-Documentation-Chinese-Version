#!/usr/bin/env python3
"""Audit official-layout alignment evidence for the RenderMan HTML docs.

The script is intentionally conservative: it can prove static invariants for all
pages and records which pages still need browser or manual visual review.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
DOCROOT = ROOT / "renderman-docs-27"
HTML_SRC = DOCROOT / "html"
HTML_ZH = DOCROOT / "html-zh"
MANIFEST = DOCROOT / "manifest.json"
OUT_JSON = DOCROOT / "official-layout-page-audit.json"
OUT_MD = DOCROOT / "official-layout-page-audit.md"

THEME_ASSETS = ("offline-docs.css", "offline-docs-data.js", "offline-docs.js")
SHELL_RESIDUAL_PATTERNS = (
    "Welcome to",
    "Let's get",
    "Browse documentation",
    "Search...",
    "Main site",
    "Filter pages",
    "Space navigation",
    "Product navigation",
    "Search documentation",
    'aria-label="Close"',
)

BROWSER_SAMPLED = {
    "index.html",
    "REN27/542212097-RenderMan 27 Documentation.html",
    "RFM27/544538625-RenderMan 27 for Maya.html",
    "RFK27/546177025-RenderMan 27 for Katana.html",
    "RFH27/544640331-RenderMan 27 for Houdini.html",
    "RFB27/544636929-RenderMan 27 for Blender.html",
    "TRA/22183944-Tractor 2.html",
    "RU/476283147-RenderMan University Home.html",
    "REN27/542212198-Installation and Licensing.html",
    "REN27/542217837-PxrLayer.html",
    "TRA/22184314-Job Author Python API.html",
    "REN27/542224403-PxrProjector.html",
    "RU/599523329-R.F. - Materials - PxrSurface.html",
    "REN27/542228829-PxrCookieLightFilter.html",
    "RU/606306371-Official Example Scenes.html",
    "RFH27/544640862-Solaris & MaterialX.html",
    "RFM27/544543965-RenderMan for Maya Release Notes.html",
    "REN27/542225854-Lighting.html",
    "REN27/542232451-Rendering.html",
    "RFM27/544543935-RenderMan for Maya API.html",
    "TRA/22184352-Release Notes.html",
    "REN27/542212252-Installing on Linux.html",
    "REN27/542228360-PxrBarnLightFilter.html",
    "REN27/542216714-PxrLayerSurface.html",
    "RFK27/546178855-PrmanObjectStatements.html",
    "RFH27/544641264-Lighting in Solaris.html",
    "REN27/542236544-txmake.html",
    "REN27/542236678-Color Management.html",
    "REN27/542213271-OpenVDB Implicit Field Plugin.html",
    "REN27/542231364-Projection Plugins.html",
    "RFB27/544639119-Projection Plugins in Blender.html",
    "RFH27/544644075-OpenVDB.html",
    "REN27/542231922-Integrators.html",
    "REN27/542231984-PxrPathTracer.html",
    "RFB27/544639822-Sample and Display Filters in Blender.html",
    "RFH27/544642120-Solaris Sample and Display Filters.html",
    "RFB27/544640279-RenderMan for Blender Release Notes.html",
    "RU/599162914-RenderMan Fundamentals.html",
    "RU/606928975-PxrSurface Fundamentals.html",
    "RU/612728846-Lighting Fundamentals.html",
    "RU/609648641-USD Models.html",
    "RU/599654509-Tutorials.html",
    "REN27/542213164-Volumes.html",
    "REN27/542213419-Rendering Clouds with Aggregate Volumes.html",
    "REN27/542220781-PxrVolume.html",
    "RFH27/544643998-Volumes.html",
    "RFH27/544644370-Volume Material.html",
    "RFM27/544541121-PxrVolume in Maya.html",
    "REN27/542225952-PxrRectLight.html",
    "REN27/542228147-PxrPortalLight.html",
    "REN27/542229813-PxrRodLightFilter.html",
    "RFB27/544638905-Mesh Lights in Blender.html",
    "RFB27/544639958-Denoiser in Blender.html",
    "RFK27/546179145-Denoiser in Katana.html",
    "RFM27/544543186-Denoiser in Maya.html",
    "RFH27/544647320-RenderMan for Houdini Release Notes.html",
    "RFK27/546179753-RenderMan for Katana Release Notes.html",
    "RU/606076995-Lama Fundamentals.html",
    "RU/405700728-USD Workflows.html",
    "RU/657621139-Treasure Denoising.html",
    "REN27/542212312-Installing on Windows.html",
    "REN27/542212390-Installing on macOS.html",
    "REN27/542212504-Installing The License Server.html",
    "REN27/542212557-Linux License Server.html",
    "REN27/542212592-macOS License Server.html",
    "REN27/542212629-Windows License Server.html",
    "REN27/542212671-Installing for Large Sites.html",
    "REN27/542229435-PxrIntMultLightFilter.html",
    "REN27/542229544-PxrRampLightFilter.html",
    "REN27/542230807-PxrGoboLightFilter.html",
    "RFH27/544641289-Light Filters in Solaris.html",
    "RFM27/544541572-Light Filters in Maya.html",
    "REN27/542213836-PxrSurface.html",
    "REN27/542221154-PxrMarschnerHair.html",
    "REN27/542222454-OSL Patterns.html",
    "REN27/542222644-PxrBlend.html",
    "RFM27/544540421-Assign materials.html",
    "RU/405700767-Character Shading Resources.html",
    "RU/657555758-Lama Skin Shading.html",
    "RU/656834683-Hippie Dragon Shading.html",
    "REN27/542215119-Diffuse Parameters.html",
    "REN27/542215275-Specular Parameters.html",
    "REN27/542215694-Glass Parameters.html",
    "REN27/542216157-Subsurface Scattering Parameters.html",
    "REN27/542219348-LamaConductor.html",
    "REN27/542219603-LamaDielectric.html",
    "REN27/542220045-LamaSheen.html",
    "REN27/542220135-LamaSSS.html",
    "REN27/542221096-PxrDisplace.html",
    "REN27/542221623-Nested Dielectrics.html",
    "REN27/542221833-Stylized Hatching.html",
    "REN27/542221920-Stylized Lines.html",
    "RFH27/544640743-Creating a Material in Solaris.html",
    "RFH27/544641395-Solaris Lighting Workflow.html",
    "RFH27/544644545-Using Material Layers.html",
    "RFK27/546178139-Material Layers in Katana.html",
    "RFK27/546179095-AOVs and Displays in Katana.html",
    "RFM27/544538696-Installation of RenderMan for Maya.html",
    "RFM27/544540223-Alembic Workflows.html",
    "RFM27/544540989-Using Material Layers.html",
    "RFM27/544541164-Using PxrOSL.html",
    "RU/599228438-R.F. - Getting Started.html",
    "RU/599523393-R.F. - Lighting.html",
    "RU/608469325-Official Swatch.html",
    "REN27/542212468-Updating Existing Installations.html",
    "REN27/542212695-Non-Commercial License Renewal.html",
    "REN27/542223700-PxrHairColor.html",
    "REN27/542225110-PxrTileManifold.html",
    "RFB27/544637465-Preset Browser in Blender.html",
    "RFB27/544640190-Examples in Blender.html",
    "RFB27/544638346-Attaching a material.html",
    "RFB27/544638473-Fur-Hair Shading in Blender.html",
    "RFH27/544640398-Installation of RenderMan for Houdini.html",
    "RFH27/544642975-Preset Browser.html",
    "RFH27/544643750-Using Primvars and Attributes.html",
    "RFH27/544645977-AOV Setup and Viewing.html",
    "RFK27/546177260-Scene Setup.html",
    "RFK27/546178005-Shading in Katana.html",
    "RFK27/546179237-Preset Browser in Katana.html",
    "RFM27/544539564-Preset Browser in Maya.html",
    "RFM27/544543762-Examples in Maya.html",
    "RU/600113153-R.F. - Materials - Lama.html",
    "RU/599523361-R.F. - Patterns.html",
    "RU/622592143-Mentoring Session Archive.html",
    "RU/604438529-Making a Toy F1 Car.html",
    "RU/632783516-Lama Car Paints.html",
    "TRA/22184226-Task Graph Pane.html",
    "TRA/22184254-Job Scripting.html",
    "TRA/22184276-tractor-spool.html",
    "TRA/22184308-Limits Configuration.html",
    "TRA/22184316-Engine.html",
    "TRA/22184341-APIs.html",
    "REN27/542215468-Clear Coat Parameters.html",
    "REN27/542215885-Iridescence Parameters.html",
    "REN27/542216422-Single Scatter Parameters.html",
    "REN27/542219129-LamaLayer.html",
    "REN27/542223198-PxrDirt.html",
    "REN27/542223474-PxrFlakes.html",
    "REN27/542225558-PxrWorley.html",
    "REN27/542226291-PxrCylinderLight.html",
    "REN27/542226975-PxrDomeLight.html",
    "REN27/542227440-PxrSphereLight.html",
    "RFB27/544639159-Motion Blur in Blender.html",
    "RFB27/544638664-Texture Reference Pose.html",
    "RFH27/544641996-Motion Blur in Solaris.html",
    "RFH27/567312445-Holdout Workflow in Solaris.html",
    "RFK27/546177126-Environment Variables in Katana.html",
    "RFK27/546178764-Render Settings in Katana.html",
    "RFM27/544541742-Motion Blur in Maya.html",
    "RFM27/544540203-About Primitive Variables.html",
    "RFM27/544541201-Texture Manager.html",
    "RU/599359489-RenderMan Kickstarters.html",
    "RU/599425025-R.F. - Color Management.html",
    "RU/604438600-Stirling VFX.html",
    "RU/608436225-Piper Beach.html",
    "RU/619642881-Best Practices - Milk Bottle.html",
    "RU/619773953-Dielectrics and Conductors.html",
    "TRA/22184250-Logging.html",
    "TRA/22184256-Job Scripting Operators.html",
    "TRA/22184260-Tractor URL API.html",
    "TRA/22184266-Query Python API.html",
    "TRA/22184280-tractor-engine.html",
    "REN27/542226613-PxrDiskLight.html",
    "REN27/542227181-PxrEnvDayLight.html",
    "REN27/542227805-PxrMeshLight.html",
    "REN27/542227947-PxrDistantLight.html",
    "REN27/542216066-Fuzz Parameters.html",
    "REN27/542216653-Glow Parameters.html",
    "REN27/542219773-LamaDiffuse.html",
    "REN27/542224293-PxrMultiTexture.html",
    "REN27/542232083-PxrUnified.html",
    "RFB27/544639651-Render Holdouts in Blender.html",
    "RFB27/544640096-Customizing Blender.html",
    "RFH27/544643009-RenderMan Shelf.html",
    "RFH27/544645263-Dome And Portal Lights.html",
    "RFH27/567279625-EnvDayLight in Solaris.html",
    "RFK27/546177488-Volumes in Katana.html",
    "RFK27/546178913-PrmanGlobalStatements.html",
    "RFK27/637632529-Stats in Katana.html",
    "RFM27/544538944-RenderMan Shelf.html",
    "RFM27/544539520-Supported Maya Nodes.html",
    "RFM27/544541101-PxrMarschnerHair in Maya.html",
    "RFM27/544543137-Image Tool or -it- in Maya.html",
    "RU/392626287-Substance Painter & RenderMan.html",
    "RU/596770821-The Smoking Gnome.html",
    "RU/611647489-Elucidae.html",
    "RU/619806721-PxrSurface - Material Layering.html",
    "RU/623509593-PxrDirt & PxrCurvature.html",
    "TRA/22184272-Directory Mapping.html",
    "TRA/22184284-NIMBY.html",
    "TRA/22184304-Custom Menu Items.html",
    "TRA/22184318-tq Cookbook.html",
    "REN27/542212781-Geometry.html",
    "REN27/542212854-Curves.html",
    "REN27/542222552-PxrAttribute.html",
    "REN27/542224582-PxrRandomTextureManifold.html",
    "REN27/542231407-PxrCamera.html",
    "REN27/542236770-Custom OCIO Config.html",
    "RFB27/544637184-Trace Sets Editor.html",
    "RFB27/544637371-Light Linking Editor.html",
    "RFB27/544637554-Aggregate Volumes in Blender.html",
    "RFB27/544639442-Interactive Rendering in Blender.html",
    "RFH27/544641499-Mesh Lights in Solaris.html",
    "RFH27/544642025-Checkpoint & Recovery.html",
    "RFH27/544645367-Cryptomatte in Houdini.html",
    "RFH27/544647025-Smoke.html",
    "RFK27/546177143-Configuring Katana.html",
    "RFK27/546177384-Custom Katana Ops.html",
    "RFK27/546179303-XGen in Katana.html",
    "RFK27/546179471-PxrMatteID in Katana.html",
    "RFM27/544540160-Geometric Settings.html",
    "RFM27/544542112-Tilt-Shift in Maya.html",
    "RFM27/544543095-Holdouts in Maya.html",
    "RFM27/544543914-Procedurals in Maya.html",
    "RU/604569601-Creating a French Bakery.html",
    "RU/604569807-Dragon Treasure.html",
    "RU/608927745-Best Practices - The Tray.html",
    "RU/637272149-Texture Randomization.html",
    "RU/654573608-Toy Car Texturing.html",
    "RU/656999009-Character Lighting Tips.html",
    "TRA/22184208-RenderMan for Maya.html",
    "TRA/22184296-PostgreSQL.html",
    "REN27/541786219-RenderMan 27 Home.html",
    "REN27/542213016-Subdivision Surfaces.html",
    "REN27/542213207-Implicit Surfaces.html",
    "REN27/542213625-Modeling Guidelines.html",
    "REN27/542219875-LamaEmission.html",
    "REN27/542219991-LamaIridescence.html",
    "REN27/542220614-Lama Metals.html",
    "REN27/542221476-Visibility.html",
    "REN27/542222597-PxrBakeTexture.html",
    "REN27/542223097-PxrCurvature.html",
    "REN27/542224176-PxrMatteID.html",
    "REN27/542225070-PxrTexture.html",
    "RFB27/544636971-Installation of RenderMan for Blender.html",
    "RFB27/544637295-String Tokens in Blender.html",
    "RFB27/544638559-Material Layering with PxrLayerSurface in Blender.html",
    "RFB27/544638999-PxrAOVLight in Blender.html",
    "RFH27/544640480-Solaris Limitations.html",
    "RFH27/544641829-Solaris Denoise Workflow.html",
    "RFH27/544643715-User Attributes.html",
    "RFH27/544644133-Implicit Surfaces.html",
    "RFK27/546177430-Error Handling.html",
    "RFK27/546177906-Instancing in Katana.html",
    "RFK27/546178343-Stylized Looks Overview Videos in Katana.html",
    "RFK27/546178826-Checkpoints and Recovery.html",
    "RFM27/544538718-Getting Started in Maya.html",
    "RFM27/544540950-PxrSurface in Maya.html",
    "RFM27/544541146-Installing Custom Nodes.html",
    "RFM27/544543262-Introduction to Best Practices.html",
    "RU/384368745-RenderMan CheatSheet.html",
    "RU/592019497-Light Randomization.html",
    "RU/608141585-Studio Lights.html",
    "TRA/22184264-JSON Job Scripting.html",
    "TRA/22184310-Checkpoint-Resume and Incremental Processing.html",
    "REN27/542220346-LamaTranslucent.html",
    "REN27/542221558-Presence and Opacity.html",
    "REN27/542222017-Stylized AOVs.html",
    "REN27/542222104-Stylized Looks Gallery.html",
    "REN27/542222617-PxrBlackBody.html",
    "REN27/542224229-PxrMix.html",
    "REN27/542224458-PxrRamp.html",
    "REN27/542224612-PxrRemap.html",
    "REN27/542224705-PxrRoundCube.html",
    "REN27/542225035-PxrTee.html",
    "RFB27/544637021-Getting Started in Blender.html",
    "RFB27/544638080-Instances.html",
    "RFB27/544638640-UDIMs in Blender.html",
    "RFB27/544638797-Lighting in Blender.html",
    "RFB27/546766879-Light Linking.html",
    "RFH27/544644871-Bokeh.html",
    "RFH27/544645130-Adding Lights.html",
    "RFH27/544645601-Checkpoints and Recovery.html",
    "RFH27/544646381-Rendering to a Device.html",
    "RFH27/544646600-Stylized Looks Overview Videos in Houdini.html",
    "RFH27/544647180-Examples in Houdini.html",
    "RFK27/546177673-Subdivision Surfaces in Katana.html",
    "RFK27/546177856-User Attributes.html",
    "RFK27/546178440-PxrAovLight in Katana.html",
    "RFK27/546178787-Thread Control in Katana.html",
    "RFK27/546179628-Copper Patina with Layered Materials.html",
    "RFM27/544539792-Instances in Maya.html",
    "RFM27/544540480-Geometric edits.html",
    "RFM27/544541347-Stylized Looks Overview Videos in Maya.html",
    "RFM27/544541535-Mesh Lights in Maya.html",
    "RFM27/544543053-Baking illumination.html",
    "RU/392265765-Procedural Ground Dirt.html",
    "RU/393805842-Creating a Wooden Floor.html",
    "RU/399245378-What Light, When-.html",
    "RU/598901006-Lighting Path.html",
    "RU/599883858-Textures.html",
    "TRA/22184210-Configuration.html",
    "TRA/22184270-Glossary.html",
    "TRA/22184288-Site Status Filter.html",
    "TRA/22184298-Creating a custom Environment Handler.html",
    "REN27/542212954-NURBS.html",
    "REN27/542212981-Polygons.html",
    "REN27/542213293-Instancing.html",
    "REN27/542219328-LamaMix.html",
    "REN27/542220578-Lama Glass.html",
    "REN27/542224051-PxrLayeredTexture.html",
    "REN27/542224088-PxrManifold3D.html",
    "REN27/542224996-PxrTangentField.html",
    "REN27/542231131-Bokeh.html",
    "REN27/542232193-PxrOcclusion.html",
    "RFB27/544637727-Archives in Blender.html",
    "RFB27/544637943-Curves.html",
    "RFB27/544638001-Subdivision Surfaces in Blender.html",
    "RFB27/544638415-Displacement in Blender.html",
    "RFB27/544639742-AOVs in Blender.html",
    "RFH27/544640499-RenderMan LOP Parameters.html",
    "RFH27/544642318-Rendering Volumes.html",
    "RFH27/544644451-OSL Patterns.html",
    "RFH27/544644832-Camera Projections.html",
    "RFH27/544645764-PDG Support.html",
    "RFH27/564199461-Stylized Looks in Solaris.html",
    "RFK27/546177441-hdPrman in Katana.html",
    "RFK27/546177706-Procedurals in Katana.html",
    "RFK27/546178051-PrmanSignalVisualizer.html",
    "RFK27/546178401-Light Arrays.html",
    "RFK27/546178966-Rendering in Katana.html",
    "RFM27/544539547-String tokens in RfM.html",
    "RFM27/544539634-Archives in Maya.html",
    "RFM27/544540797-ZBrush Vector Displacement.html",
    "RFM27/544541369-Lighting in Maya.html",
    "RFM27/544542501-AOVs.html",
    "RU/568557635-The Hunted Refs.html",
    "RU/600145995-Projects.html",
    "RU/604635137-Sorindar, the Gray Rock Dragon.html",
    "RU/604667905-Hippie The Forest Dragon.html",
    "RU/608632849-Introduction to Best Practices.html",
    "RU/629932059-What is Path Tracing-.html",
    "RU/654639145-Toy Car Modeling.html",
    "TRA/22184248-Troubleshooting.html",
    "TRA/22184290-Blade Environment Configuration- Keys and Handlers.html",
    "TRA/22184294-Crews.html",
    "TRA/22184322-Login Management.html",
    "REN27/542212717-RenderMan.html",
    "REN27/542213120-Particles.html",
    "REN27/542213347-Aggregate Volumes.html",
    "REN27/542213678-Shading.html",
    "REN27/542213758-Pixar Surface Materials.html",
    "REN27/542218974-PxrLayerMixer.html",
    "REN27/542218994-MaterialX Lama.html",
    "REN27/542219059-MaterialX Lama Layering.html",
    "REN27/542219300-LamaAdd.html",
    "REN27/542219925-LamaGeneralizedSchlick.html",
    "REN27/542219952-LamaHairChiang.html",
    "REN27/542220286-LamaSurface.html",
    "REN27/542220410-LamaTricolorSSS.html",
    "REN27/542220441-Lama Material Examples.html",
    "REN27/542220700-LamaLPE.html",
    "REN27/542221690-Stylized Looks.html",
    "RFB27/544374874-Blender 27 Home.html",
    "RFB27/544637109-User Interface in Blender.html",
    "RFB27/544637132-Workspace in Blender.html",
    "RFB27/544637312-Light Mixer Editor.html",
    "RFB27/544637526-Geometry in Blender.html",
    "RFB27/544637617-Quadrics in Blender.html",
    "RFB27/544637646-Procedural Primitives in Blender.html",
    "RFB27/544637687-OpenVDB Volumes in Blender.html",
    "RFH27/544505959-Houdini 27 Home.html",
    "RFH27/544640429-Solaris.html",
    "RFH27/544640549-Geometry in Solaris.html",
    "RFH27/544640572-Solaris Geometry Workflow.html",
    "RFH27/544640621-Adding Displacement.html",
    "RFH27/544640652-Adding Subdivision.html",
    "RFH27/544640696-Render Geometry Settings.html",
    "RFH27/544640718-Shading in Solaris.html",
    "RFH27/544640830-Rendering SOP Volumes.html",
    "RFH27/544640896-Converting Textures.html",
    "RFK27/544342321-Katana 27 Home.html",
    "RFK27/546177107-Installation of RenderMan for Katana.html",
    "RFK27/546177369-Upgrading scenes from RenderMan 24 to 27.html",
    "RFK27/546177401-PrmanOpDebug.html",
    "RFK27/546177458-Geometry in Katana.html",
    "RFM27/544243817-Maya 27 Home.html",
    "RFM27/544538919-User Interface in Maya.html",
    "RFM27/544539259-RenderMan Menu.html",
    "RFM27/544539308-RenderMan Preferences.html",
    "RFM27/544539366-Prefs - Render.html",
    "RU/392822785-Controlling Textures.html",
    "RU/392953857-Neons.html",
    "RU/399343692-Denoising guide.html",
    "RU/405569811-Look 2.html",
    "TRA/22184212-Connections.html",
    "TRA/22184214-Job List Pane.html",
    "TRA/22184216-Job Info Pane.html",
    "TRA/22184218-Tractor UI Tour.html",
    "REN27/542220715-MaterialX.html",
    "REN27/542220743-PxrDisneyBsdf.html",
    "REN27/542221735-Getting Started with Stylized Looks.html",
    "REN27/542221812-Stylized Canvas.html",
    "REN27/542221952-Stylized Toon.html",
    "REN27/542221999-Stylized Control.html",
    "REN27/542222258-Patterns.html",
    "REN27/542222405-aaOceanPrmanShader.html",
    "REN27/542222488-PxrAdjustNormal.html",
    "REN27/542222537-PxrArithmetic.html",
    "REN27/542222579-PxrBakePointCloud.html",
    "REN27/542222811-PxrBlenderPrincipledInputs.html",
    "REN27/542222840-PxrBump.html",
    "REN27/542222866-PxrBumpManifold2D.html",
    "REN27/542222881-PxrBumpMixer.html",
    "REN27/542222907-PxrBumpRoughness.html",
    "REN27/542222962-PxrChecker.html",
    "REN27/542223021-PxrClamp.html",
    "RFB27/544638169-Particles.html",
    "RFB27/544638243-Shading in Blender.html",
    "RFB27/544638744-Stylized Looks in Blender.html",
    "RFB27/544638842-Light Filters in Blender.html",
    "RFB27/544638952-Analytic Lights in Blender.html",
    "RFB27/544639096-Cameras in Blender.html",
    "RFB27/544639374-Depth of Field in Blender.html",
    "RFB27/544639419-Rendering in Blender.html",
    "RFB27/544639612-Batch Rendering in Blender.html",
    "RFB27/544639698-Baking in Blender.html",
    "RFB27/544639892-Integrators in Blender.html",
    "RFB27/544640056-Advanced.html",
    "RFB27/544640079-GitHub Nightlies.html",
    "RFB27/544640138-Reporting Bugs.html",
    "RFH27/544640927-Preset Browser in Solaris.html",
    "RFH27/544641013-Solo Material - Patterns.html",
    "RFH27/544641152-Cameras in Solaris.html",
    "RFH27/544641181-PxrCamera.html",
    "RFH27/544641475-Light Linking in Solaris.html",
    "RFH27/544641728-Rendering in Solaris.html",
    "RFH27/544641753-Solaris Render Settings.html",
    "RFH27/544641793-Interactive Denoiser in Solaris.html",
    "RFH27/544641953-Setting up LPEs in Solaris.html",
    "RFH27/544642079-Cryptomatte in Solaris.html",
    "RFK27/546177622-Aggregate Volumes in Katana.html",
    "RFK27/546177753-Polygons in Katana.html",
    "RFK27/546177781-Curves in Katana.html",
    "RFK27/546177835-Geometric Settings.html",
    "RFK27/546177881-Primitive Variables.html",
    "RFK27/546177992-Particles in Katana.html",
    "RFM27/544539402-Prefs - Workflow.html",
    "RFM27/544539420-Prefs - User Interface.html",
    "RFM27/544539452-Prefs - Viewport.html",
    "RFM27/544539475-Prefs - OpenColorIO.html",
    "RU/405668093-Look 3.html",
    "RU/405700944-Stylization.html",
    "TRA/22184220-About Tractor Pane.html",
    "TRA/22184222-Blade List Pane.html",
    "REN27/542223036-PxrColorCorrect.html",
    "REN27/542223051-PxrColorGrade.html",
    "REN27/542223066-PxrColorSpace.html",
    "REN27/542223082-PxrCross.html",
    "REN27/542223338-PxrDispScalarLayer.html",
    "REN27/542223359-PxrDispTransform.html",
    "REN27/542223392-PxrDispVectorLayer.html",
    "REN27/542223417-PxrDot.html",
    "REN27/542223428-PxrEnvGround.html",
    "REN27/542223444-PxrExposure.html",
    "REN27/542223459-PxrFacingRatio.html",
    "REN27/542223600-PxrFractal.html",
    "REN27/542223657-PxrGamma.html",
    "REN27/542223668-PxrGeometricAOV.html",
    "REN27/542223682-PxrGrid.html",
    "REN27/542223991-PxrHexTileManifold.html",
    "REN27/542224012-PxrHSL.html",
    "REN27/542224027-PxrInvert.html",
    "REN27/542224038-PxrLayeredBlend.html",
    "REN27/542224071-PxrManifold2D.html",
    "REN27/542224201-PxrMetallicWorkflow.html",
    "REN27/542224317-PxrNormalMap.html",
    "REN27/542224343-PxrPhasorNoise.html",
    "REN27/542224365-PxrPrimvar.html",
    "RFH27/544642213-Pref in Solaris.html",
    "RFH27/544642250-Live Stats in Solaris.html",
    "RFH27/544642287-Tractor Spool Panel.html",
    "RFH27/544642517-Solaris Studio.html",
    "RFH27/544642603-Studio Breakdown.html",
    "RFH27/544642618-Assembly Stage.html",
    "RFH27/544642665-Layout Stage.html",
    "RFH27/544642691-Lighting Stage.html",
    "RFH27/544642725-Examples in Solaris.html",
    "RFH27/544642760-RfH Classic.html",
    "RFH27/544642790-Getting Started in Houdini.html",
    "RFH27/544642900-Getting Help.html",
    "RFH27/544642937-User Interface in Houdini.html",
    "RFK27/546178105-Using Displacement.html",
    "RFK27/546178221-Surface Orientation.html",
    "RFK27/546178276-Stylized Looks in Katana.html",
    "RFK27/546178301-Stylized Looks in Katana Overview.html",
    "RFK27/546178364-Lighting in Katana.html",
    "RFK27/546178425-Shortcuts in Katana.html",
    "RFM27/544539497-Prefs - Preset Browser.html",
    "RFM27/544539616-Geometry in Maya.html",
    "RFM27/544539731-Curves in Maya.html",
    "RFM27/544539956-Particles in Maya.html",
    "RFM27/544539991-Subdivision Surfaces in Maya.html",
    "RFM27/544540066-OpenVDB Volumes in Maya.html",
    "RFM27/544540118-Aggregate Volumes in Maya.html",
    "RU/405700954-Look 1.html",
    "RU/405733531-Samples made Simple.html",
    "RU/405864738-Getting Started with Stylization.html",
    "RU/502759691-Procedural Edge Breakup.html",
    "RU/506298373-External Learning.html",
    "TRA/22184224-Blade Info Pane.html",
    "TRA/22184228-Task Info Pane.html",
    "TRA/22184230-Query Pane.html",
    "TRA/22184232-Data Filtering.html",
    "TRA/22184234-Blade Activity Pane.html",
    "TRA/22184236-Engine Metrics.html",
    "TRA/22184238-Admin.html",
    "REN27/542224380-PxrProjectionLayer.html",
    "REN27/542224392-PxrProjectionStack.html",
    "REN27/542224432-PxrPtexture.html",
    "REN27/542224443-PxrRadialDensity.html",
    "REN27/542224681-PxrRGBtoNG.html",
    "REN27/542224902-PxrShadedSide.html",
    "REN27/542224924-PxrSplineMap.html",
    "REN27/542224935-PxrStylizedControl.html",
    "REN27/542224974-PxrSwitch.html",
    "REN27/542225088-PxrThinFilm.html",
    "REN27/542225099-PxrThreshold.html",
    "REN27/542225447-PxrToFloat.html",
    "REN27/542225462-PxrToFloat3.html",
    "REN27/542225473-PxrVariable.html",
    "REN27/542225490-PxrVary.html",
    "REN27/542225517-PxrVoronoise.html",
    "REN27/542225547-PxrWireframe.html",
    "REN27/542228318-PxrAOVLight.html",
    "REN27/542228334-Light Filters.html",
    "REN27/542231003-Shadows.html",
    "REN27/542231085-Cameras.html",
    "REN27/542231237-Depth of Field.html",
    "REN27/542231276-Shutter.html",
    "REN27/542231325-The Viewing Transformation.html",
    "REN27/542231487-Aperture.html",
    "REN27/542231583-Tilt-Shift.html",
    "REN27/542231607-Lens Distortion.html",
    "REN27/542231686-DOF Distortion.html",
    "REN27/542231710-Split Diopter.html",
    "REN27/542231739-Chromatic Aberration.html",
    "REN27/542231763-Vignetting.html",
    "REN27/542231817-Camera Shutter.html",
    "REN27/542231837-PxrCamera Advanced.html",
    "REN27/542231854-Enhance.html",
    "REN27/542231871-PxrPanini.html",
    "REN27/542232008-PxrVCM.html",
    "REN27/542232143-Using Manifold Walk.html",
    "REN27/542232400-PxrVisualizer.html",
    "REN27/542235274-PxrCryptomatte.html",
    "REN27/542238759-542238759.html",
    "RFK27/546178489-Portal Lights in Katana.html",
    "RFK27/546178518-Mesh Lights in Katana.html",
    "RFK27/546178552-Light Filters in Katana.html",
    "RFK27/546178609-PxrBarnLightFilter in Katana.html",
    "RFK27/546178629-Cameras in Katana.html",
    "RFK27/546178644-Motion Blur in Katana.html",
    "RFK27/546178680-Display & Sample Filters in Katana.html",
    "RFK27/546178709-Camera Settings in Katana.html",
    "RFK27/546178888-PrmanIntegratorSettings.html",
    "RFK27/546178939-XPU in Katana.html",
    "RFK27/546179038-Holdouts in Katana.html",
    "RFK27/546179060-Baking in Katana.html",
    "RFK27/546179198-Interactive Denoiser.html",
    "RFK27/546179286-Tutorials in Katana.html",
    "RFK27/546179420-Using PxrVary.html",
    "RFK27/546179539-Houdini motion blur in RfK.html",
    "RFK27/546179578-Cryptomatte in Katana.html",
    "RFK27/546179662-Examples in Katana.html",
    "RFK27/628719654-Export to RIB.html",
    "TRA/22184240-Limit Counters.html",
    "TRA/22184242-Preferences.html",
    "TRA/22184244-Administration Pane.html",
    "TRA/22184246-RMS.html",
    "TRA/22184252-Alternative Authentication.html",
    "TRA/22184258-Idle Job or Task.html",
    "TRA/22184262-Search Clauses.html",
    "TRA/22184274-tractor-blade.html",
    "TRA/22184278-Your First Job.html",
    "TRA/22184282-Dashboard App.html",
    "TRA/22184286-tractor-dbctl.html",
    "TRA/22184292-Blades.html",
    "RFH27/544643524-RenderMan Menu.html",
    "RFH27/544643561-RenderMan Preferences.html",
    "RFH27/544643585-Geometry in Houdini.html",
    "RFH27/544643637-Geometric Settings.html",
    "RFH27/544643653-Grouping Membership.html",
    "RFH27/544643704-Setting Pref.html",
    "RFH27/544643849-Curves.html",
    "RFH27/544643901-Fur and Hair in Houdini.html",
    "RFH27/544644033-Aggregate Volumes.html",
    "RFH27/544644151-Particles.html",
    "RFH27/544644181-Instances.html",
    "RFH27/544644237-Subdivision Surfaces.html",
    "RFH27/544644296-Shading in Houdini.html",
    "RFH27/544644341-Texture Manager.html",
    "RFH27/544644429-Soloing Patterns.html",
    "RFH27/544644486-Assigning Materials To Faces.html",
    "RFH27/544644642-Using Displacement.html",
    "RFH27/544644703-Creating A Material.html",
    "RFH27/544644797-Cameras in Houdini.html",
    "RFH27/544644900-Depth of Field.html",
    "RFH27/544644938-Using Motion Blur.html",
    "RFH27/544644982-Lighting in Houdini.html",
    "RFH27/544645013-Light Linking.html",
    "RFH27/544645033-Light Filters.html",
    "RFH27/544645211-AOV Light.html",
    "RFH27/544645281-Rendering in Houdini.html",
    "RFH27/544645311-Denoiser in Houdini.html",
    "RFH27/544645351-Workflows.html",
    "RFH27/544645461-Holdouts.html",
    "RFH27/544645511-Baking.html",
    "RFH27/544645844-Display & Sample Filters.html",
    "RFH27/544645926-Output.html",
    "RFH27/544646093-Options.html",
    "RFH27/544646109-Output (Legacy) Statistics.html",
    "RFH27/544646266-Setup.html",
    "RFH27/544646324-Export to RIB.html",
    "RFH27/544646437-The ROP Node.html",
    "RFH27/544646515-Stylized Looks in Houdini.html",
    "RFH27/544646545-Stylized Looks in Houdini Overview.html",
    "RFH27/544646622-How-Tos for Houdini.html",
    "RFH27/544646645-Exporting Ri Attributes.html",
    "RFH27/544646676-Using PxrMatteID.html",
    "RFH27/544646740-Coordinate System.html",
    "RFH27/544646763-Kaboom Box HDA.html",
    "RFH27/544646810-Feature Tabs.html",
    "RFH27/544646833-Export.html",
    "RFH27/544646865-Bindings.html",
    "RFH27/544646892-Render.html",
    "RFH27/544646941-Fire.html",
    "RFH27/544646978-Scatter.html",
    "RFH27/544647115-Kaboom Box Kickstarter.html",
    "RFH27/544647152-Installation.html",
    "RFH27/544647276-TroubleShooting & Tips.html",
    "RFH27/544647299-Frequently Asked Questions.html",
    "RFH27/567050268-Portal Lights in Solaris.html",
    "RFH27/575406115-PxrAovLight in Solaris.html",
    "RFH27/575569950-Integrators in Solaris.html",
    "RFH27/634748959-RenderMan Render Settings.html",
    "RFM27/544540557-Shading in Maya.html",
    "RFM27/544540613-Maya File Node.html",
    "RFM27/544540645-Pixar Patterns.html",
    "RFM27/544540663-Using Displacement.html",
    "RFM27/544540737-Mudbox Vector Displacement.html",
    "RFM27/544541251-MaterialX Lama in Maya.html",
    "RFM27/544541276-Stylized Looks in Maya.html",
    "RFM27/544541301-Stylized Looks in Maya Overview.html",
    "RFM27/544541437-Analytic Lights in Maya.html",
    "RFM27/544541661-PxrAOVLight in Maya.html",
    "RFM27/544541707-Cameras in Maya.html",
    "RFM27/544541982-Depth of Field in Maya.html",
    "RFM27/544542056-Bokeh in Maya.html",
    "RFM27/544542258-Projections in Maya.html",
    "RFM27/544542282-Render Settings in Maya.html",
    "RFM27/544542322-Common.html",
    "RFM27/544542378-Sampling.html",
    "RFM27/544542444-Features.html",
    "RFM27/544542604-Custom AOV Creation.html",
    "RFM27/544542672-Advanced.html",
    "RFM27/544542704-Workspace.html",
    "RFM27/544542739-Rendering in Maya.html",
    "RFM27/544542770-Preview Rendering in Maya.html",
    "RFM27/544542819-Interactive Rendering in Maya.html",
    "RFM27/544542924-Interactive Denoiser in Maya.html",
    "RFM27/544542955-Batch Rendering in Maya.html",
    "RFM27/544543018-Baking in Maya.html",
    "RFM27/544543164-Manual RIB Export.html",
    "RFM27/544543235-Tutorials in Maya.html",
    "RFM27/544543508-MatteID in Maya.html",
    "RFM27/544543597-Variation of Instances in Maya.html",
    "RFM27/544543618-Cryptomatte in Maya.html",
    "RFM27/544543656-Using Trace Sets in Maya.html",
    "RFM27/544543898-Developer's Guide for Maya.html",
    "TRA/22184300-Example Envrionment Handler.html",
    "TRA/22184302-Scheduling Modes.html",
    "TRA/22184306-tq- Tractor Query tool.html",
    "TRA/22184312-Server Profiles.html",
    "TRA/22184320-Administration.html",
    "TRA/22184324-Advanced Blade Capability Advertisement.html",
    "TRA/22184326-Initial Configuration.html",
    "TRA/22184328-Setting Up Services.html",
    "TRA/22184330-Dashboard.html",
    "TRA/22184332-Image Preview.html",
    "TRA/22184334-Getting Started.html",
    "TRA/22184336-Installation.html",
    "TRA/22184339-About Tractor.html",
    "TRA/22184343-Appendix.html",
    "TRA/22184346-Applications.html",
    "TRA/22184348-Upgrading.html",
    "TRA/22184350-Upgrading from Tractor 1.x.html",
    "TRA/22184354-Tractor 2 Features.html",
    "TRA/22184356-Implementation.html",
    "TRA/22184358-Upgrading to 2.1.html",
    "TRA/22184360-Upgrading to 2.2.html",
    "TRA/22184362-System Requirements.html",
    "TRA/22186899-RenderMan Documentation.mobile.phone.html",
    "TRA/22191840-brikit.mobile.html",
    "TRA/22191842-Contents.html",
    "RU/562757686-RenderMan Demo Sign.html",
    "RU/562823215-The Hunted.html",
    "RU/563118083-The Hunted Van.html",
    "RU/563478530-The Hunted Story.html",
    "RU/567017582-The Hunted Finalizing.html",
    "RU/567083091-The Hunted Lighting.html",
    "RU/567279687-The Hunted USD Worfklow.html",
    "RU/567509003-The Hunted Texturing.html",
    "RU/567509019-The Hunted Layout.html",
    "RU/568557622-Adding Wonder!.html",
    "RU/568787000-Start with Words.html",
    "RU/569278526-Idea Seeds.html",
    "RU/573505543-RenderMan Art Challenge.html",
    "RU/591691817-Light Bulbs.html",
    "RU/592183305-Sign Shading.html",
    "RU/592216069-Neon Modelling.html",
    "RU/597491715-Guest Scenes.html",
    "RU/598901015-Rendering Path.html",
    "RU/599163154-Shading Path.html",
    "RU/599163179-PxrSurface.html",
    "RU/599163195-Procedural.html",
    "RU/599261185-New to RenderMan-.html",
    "RU/599654499-MaterialX Lama.html",
    "RU/600113185-Resources.html",
    "RU/600113259-Texture Maps.html",
    "RU/600113366-Materials & Presets.html",
    "RU/600145921-Learning Paths.html",
    "RU/600178689-HDRIs.html",
    "RU/600211457-Light Rigs.html",
    "RU/606175285-Lama Layer Storytelling.html",
    "RU/606208122-Lama Metallic Workflow.html",
    "RU/606240829-RenderMan Wallpapers.html",
    "RU/606240846-Lama Metals.html",
    "RU/606339097-Fun Stuff.html",
    "RU/606502995-Lama Plastics.html",
    "RU/607879203-RenderMan Digital Studio.html",
    "RU/608272385-Cookies & Milk.html",
    "RU/608272451-The Hidden People.html",
    "RU/608305153-Louise.html",
    "RU/608305219-Crocostrich.html",
    "RU/608305285-Fridge.html",
    "RU/608305351-Onward Teapot.html",
    "RU/608337921-Stirling.html",
    "RU/608337987-Ship Shape.html",
    "RU/608403457-IES Profiles.html",
    "RU/608436284-Lac d'Annecy.html",
    "RU/608468993-Slussen.html",
    "RU/608469073-Berns Red Room.html",
    "RU/608469173-Stylized Lights.html",
    "RU/608469242-HDR Vault.html",
    "RU/608534529-Charles XII.html",
    "RU/608534614-St Eriksbron.html",
    "RU/608567297-Luxo Jr.html",
    "RU/608600070-About RenderMan University.html",
    "RU/608796673-Texture Basics.html",
    "RU/608796697-Best Practices - PxrSurface.html",
    "RU/608829441-Best Practices - Modeling.html",
    "RU/608829457-Best Practices - Wood Table.html",
    "RU/608862209-Best Practices - Textures.html",
    "RU/609157121-Grunge Maps Vol.1.html",
    "RU/611647560-Kaboom Box.html",
    "RU/611680257-SciTech Scene.html",
    "RU/611680348-Taraji.html",
    "RU/611713025-Dragon Plush.html",
    "RU/612401313-PxrSurface - Glass.html",
    "RU/619708417-Best Practices - The Milk.html",
    "RU/619708556-Best Practices - Lighting.html",
    "RU/619741185-Best Practices - Cookies.html",
    "RU/619741326-PxrSurface - Metallic Workflow.html",
    "RU/623607817-Patterns & Noises.html",
    "RU/624918545-Shading Practical Lessons.html",
    "RU/625672304-Black & White.html",
    "RU/628752397-Light Filters.html",
    "RU/629571614-Rendering Basics.html",
    "RU/630915278-Interactive Rendering Tips.html",
    "RU/631242816-The Three Light Types.html",
    "RU/631308308-Modeling Guidelines.html",
    "RU/638877713-Flashy Neons.html",
    "RU/654639152-Toy Car Shading.html",
    "RU/654671935-Toy Car Rendering.html",
    "RU/654868513-Toy Car Compositing.html",
    "RU/655065134-Toy Car Lighting.html",
    "RU/656834654-Treasure Scattering.html",
    "RU/656834669-Dragon Lighting.html",
    "RU/656834796-RazorBack Shading Pt.2.html",
    "RU/656998424-Stirling Lighting.html",
    "RU/656998438-Stirling HDRI Cleanup.html",
    "RU/656998602-Bakery Texturing.html",
    "RU/656998911-RazorBack Lighting.html",
    "RU/657162271-Stirling Compositing.html",
    "RU/657162324-Treasure Rendering.html",
    "RU/657162354-Dragon Rendering.html",
    "RU/657162426-Hippie Dragon References.html",
    "RU/657162498-RazorBack Modeling.html",
    "RU/657162522-RazorBack Displacement.html",
    "RU/657162564-RazorBack Compositing.html",
    "RU/657227810-Stirling Color Management.html",
    "RU/657227817-Stirling Texturing.html",
    "RU/657227944-Bakery Lighting.html",
    "RU/657227977-Treasure Optimizations.html",
    "RU/657228205-RazorBack Texturing.html",
    "RU/657228220-RazorBack Shading Pt.1.html",
    "RU/657228237-RazorBack Rendering.html",
    "RU/657260714-Hippe Dragon Texturing.html",
    "RU/657391677-Treasure Shading.html",
    "RU/657391684-Treasure AOVs.html",
    "RU/657391698-Treasure Deep Workflow.html",
    "RU/657391746-Hippie Dragon Modeling.html",
    "RU/657391753-Hippie Dragon Posing.html",
    "RU/657424403-Stirling Rendering.html",
    "RU/657424415-Bakery Modeling.html",
    "RU/657424423-Bakery Shading.html",
    "RU/657424439-Bakery Rendering.html",
    "RU/657424515-Treasure Environment.html",
    "RU/657555575-Dragon Modeling.html",
    "RU/657555620-RazorBack Procedural Texturing.html",
    "RU/657621053-Bakery Compositing.html",
    "RU/657621209-Dragon Texturing.html",
    "RU/657621227-Dragon Compositing.html",
    "RU/657850369-Hippie Dragon Lighting.html",
    "RU/657981441-RazorBack Whiptail.html",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def attr_map(attrs: list[tuple[str, str | None]]) -> dict[str, str]:
    return {k.lower(): v or "" for k, v in attrs}


def class_tokens(attrs: dict[str, str]) -> set[str]:
    return set(attrs.get("class", "").split())


class ArticleTagParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_article = False
        self.article_seen = False
        self.in_main = False
        self.main_seen = False
        self.capture_body = False
        self.skip_depth = 0
        self.tags: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag == "body":
            self.capture_body = True
        if tag == "main" and not self.article_seen:
            self.in_main = True
            self.main_seen = True
        if tag == "article":
            self.in_article = True
            self.article_seen = True
        capturing = self.in_article or (
            self.in_main and not self.article_seen
        ) or (self.capture_body and not self.article_seen and not self.main_seen)
        if capturing and tag in {"script", "style"}:
            self.skip_depth += 1
        if capturing and not self.skip_depth and tag not in {"script", "style"}:
            self.tags.append(tag)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if (self.in_article or self.in_main or self.capture_body) and tag in {"script", "style"} and self.skip_depth:
            self.skip_depth -= 1
        if tag == "article":
            self.in_article = False
        if tag == "main":
            self.in_main = False
        if tag == "body":
            self.capture_body = False


@dataclass
class PageFeatures:
    title: str = ""
    body_classes: set[str] = field(default_factory=set)
    links: list[str] = field(default_factory=list)
    resource_sources: list[str] = field(default_factory=list)
    scripts: list[str] = field(default_factory=list)
    stylesheets: list[str] = field(default_factory=list)
    image_sources: list[str] = field(default_factory=list)
    source_meta_count: int = 0
    article_counts: Counter[str] = field(default_factory=Counter)
    info_macros: int = 0
    expand_containers: int = 0
    childpage_links: int = 0
    in_title: bool = False
    in_article: bool = False


class FeatureParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.features = PageFeatures()

    def handle_starttag(self, tag: str, attrs_raw: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        attrs = attr_map(attrs_raw)
        classes = class_tokens(attrs)
        if tag == "title":
            self.features.in_title = True
        if tag == "body":
            self.features.body_classes = classes
        if tag == "article":
            self.features.in_article = True
        if tag == "a":
            self.features.links.append(attrs.get("href", ""))
        if "src" in attrs and tag not in {"script"}:
            self.features.resource_sources.append(attrs.get("src", ""))
        if tag == "script":
            self.features.scripts.append(attrs.get("src", ""))
        if tag == "link" and attrs.get("rel", "").lower() == "stylesheet":
            self.features.stylesheets.append(attrs.get("href", ""))
        if tag == "img":
            self.features.image_sources.append(attrs.get("src", ""))
        if "source" in classes:
            self.features.source_meta_count += 1
        if self.features.in_article:
            self.features.article_counts[tag] += 1
            if classes & {
                "confluence-information-macro",
                "confluence-information-macro-note",
                "confluence-information-macro-warning",
                "confluence-information-macro-tip",
                "confluence-information-macro-information",
            }:
                self.features.info_macros += 1
            if "expand-container" in classes:
                self.features.expand_containers += 1
            if "childpages-macro" in classes:
                self.features.childpage_links += 1

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title":
            self.features.in_title = False
        if tag == "article":
            self.features.in_article = False

    def handle_data(self, data: str) -> None:
        if self.features.in_title:
            self.features.title += data


def article_signature(path: Path) -> tuple[Counter[str], list[str]]:
    parser = ArticleTagParser()
    parser.feed(read_text(path))
    return Counter(parser.tags), parser.tags


def features(path: Path) -> PageFeatures:
    parser = FeatureParser()
    parser.feed(read_text(path))
    parser.features.title = re.sub(r"\s+", " ", parser.features.title).strip()
    return parser.features


def manifest_pages() -> dict[str, dict[str, str]]:
    data = json.loads(read_text(MANIFEST))
    out: dict[str, dict[str, str]] = {}
    for page in data.get("pages", []):
        rel = str(Path(page["html_path"]).relative_to("html"))
        out[rel] = {
            "source_url": page.get("source_url", ""),
            "space_key": page.get("space_key", ""),
            "page_id": page.get("page_id", ""),
            "title": page.get("title", ""),
        }
    out.setdefault(
        "index.html",
        {
            "source_url": data.get("source", "https://rmanwiki-27.pixar.com"),
            "space_key": "HOME",
            "page_id": "",
            "title": "RenderMan 27 Documentation",
        },
    )
    return out


def resolve_local_asset(page: Path, src: str) -> Path | None:
    if not src or src.startswith(("http://", "https://", "data:", "mailto:", "#")):
        return None
    parsed = urlparse(src)
    if parsed.scheme:
        return None
    local = unquote(parsed.path)
    if local.startswith("/"):
        return None
    return (page.parent / local).resolve()


def classify_page(rel: str, feat: PageFeatures) -> list[str]:
    labels: list[str] = []
    if rel == "index.html":
        labels.append("home")
    if feat.article_counts["table"]:
        labels.append("table")
    if feat.article_counts["pre"]:
        labels.append("code")
    if feat.article_counts["img"] >= 20:
        labels.append("image-heavy")
    elif feat.article_counts["img"]:
        labels.append("image")
    if feat.article_counts["iframe"]:
        labels.append("iframe")
    if feat.info_macros:
        labels.append("info-panel")
    if feat.expand_containers:
        labels.append("expand")
    if not labels:
        labels.append("article")
    return labels


def audit_page(rel: Path, meta: dict[str, dict[str, str]]) -> dict[str, object]:
    rel_s = rel.as_posix()
    src_path = HTML_SRC / rel
    zh_path = HTML_ZH / rel
    issues: list[str] = []
    warnings: list[str] = []
    row: dict[str, object] = {
        "path": rel_s,
        "source_url": meta.get(rel_s, {}).get("source_url", ""),
        "space_key": meta.get(rel_s, {}).get("space_key", rel.parts[0] if len(rel.parts) > 1 else "HOME"),
        "title": meta.get(rel_s, {}).get("title", ""),
        "browser_visual_status": "passed_sample" if rel_s in BROWSER_SAMPLED else "pending",
    }

    if not src_path.exists():
        issues.append("missing_source_html")
    if not zh_path.exists():
        issues.append("missing_translated_html")
        row["static_status"] = "fail"
        row["issues"] = issues
        row["warnings"] = warnings
        return row

    text = read_text(zh_path)
    feat = features(zh_path)
    row["title"] = row["title"] or feat.title
    row["classes"] = classify_page(rel_s, feat)
    row["feature_counts"] = {
        "tables": feat.article_counts["table"],
        "pre": feat.article_counts["pre"],
        "images": feat.article_counts["img"],
        "iframes": feat.article_counts["iframe"],
        "info_macros": feat.info_macros,
        "expand_containers": feat.expand_containers,
    }

    if "rm-themed" not in feat.body_classes:
        issues.append("missing_rm_themed_body_class")
    expected_class = "rm-home" if rel_s == "index.html" else "rm-doc-page"
    if expected_class not in feat.body_classes:
        issues.append(f"missing_{expected_class}_body_class")

    for asset in THEME_ASSETS:
        if asset not in text:
            issues.append(f"missing_theme_asset:{asset}")

    for pattern in SHELL_RESIDUAL_PATTERNS:
        if pattern in text:
            issues.append(f"checked_english_residual:{pattern}")

    if rel_s != "index.html" and src_path.exists():
        src_count, src_seq = article_signature(src_path)
        zh_count, zh_seq = article_signature(zh_path)
        if src_count != zh_count:
            issues.append("article_tag_count_mismatch")
            row["tag_count_delta"] = dict((src_count - zh_count) or (zh_count - src_count))
        elif src_seq != zh_seq:
            issues.append("article_tag_sequence_mismatch")

    missing_images: list[str] = []
    for src in feat.image_sources:
        resolved = resolve_local_asset(zh_path, src)
        if resolved and not resolved.exists():
            missing_images.append(src)
    if missing_images:
        issues.append("missing_local_images")
        row["missing_local_images"] = missing_images[:10]

    if feat.source_meta_count:
        warnings.append(f"download_metadata_present_in_html:{feat.source_meta_count}")

    confluence_links = [href for href in feat.links if href.startswith("/wiki/")]
    if confluence_links:
        warnings.append(f"unrewritten_confluence_links:{len(confluence_links)}")

    confluence_resource_sources = [src for src in feat.resource_sources if src.startswith("/wiki/")]
    if confluence_resource_sources:
        issues.append("unrewritten_confluence_resource_sources")
        row["unrewritten_confluence_resource_sources"] = confluence_resource_sources[:10]

    row["static_status"] = "pass" if not issues else "fail"
    row["issues"] = issues
    row["warnings"] = warnings
    return row


def write_markdown(report: dict[str, object]) -> None:
    summary = report["summary"]
    pages = report["pages"]
    pending = [p for p in pages if p["browser_visual_status"] == "pending"]
    failed = [p for p in pages if p["static_status"] != "pass"]
    sampled = [p for p in pages if p["browser_visual_status"] == "passed_sample"]
    lines = [
        "# RenderMan 27 Official Layout Page Audit",
        "",
        "This file is generated by `tools/audit_official_layout_alignment.py`.",
        "",
        "## Summary",
        "",
        f"- Total translated HTML pages: {summary['total_pages']}",
        f"- Static pass: {summary['static_pass']}",
        f"- Static fail: {summary['static_fail']}",
        f"- Browser visual sampled pass: {summary['browser_sampled_pass']}",
        f"- Browser/manual visual pending: {summary['browser_visual_pending']}",
        f"- Pages with downloader metadata in HTML: {summary['pages_with_download_metadata']}",
        f"- Pages with unrewritten Confluence body links: {summary['pages_with_unrewritten_confluence_links']}",
        "",
        "## Static Failures",
        "",
    ]
    if failed:
        for page in failed[:80]:
            lines.append(f"- `{page['path']}`: {', '.join(page['issues'])}")
        if len(failed) > 80:
            lines.append(f"- ... {len(failed) - 80} more")
    else:
        lines.append("- None.")
    lines.extend(["", "## Browser-Sampled Pages", ""])
    for page in sampled:
        labels = ", ".join(page.get("classes", []))
        lines.append(f"- `{page['path']}` ({labels})")
    lines.extend(["", "## Next Visual-Pending Pages", ""])
    for page in pending[:80]:
        labels = ", ".join(page.get("classes", []))
        lines.append(f"- `{page['path']}` ({labels})")
    if len(pending) > 80:
        lines.append(f"- ... {len(pending) - 80} more")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    meta = manifest_pages()
    src_pages = {p.relative_to(HTML_SRC) for p in HTML_SRC.rglob("*.html")}
    zh_pages = {p.relative_to(HTML_ZH) for p in HTML_ZH.rglob("*.html") if p.relative_to(HTML_ZH).parts[0] != "assets"}
    all_pages = sorted(src_pages | zh_pages)
    pages = [audit_page(rel, meta) for rel in all_pages]
    pages_with_download_metadata = sum(
        1 for p in pages if any(str(w).startswith("download_metadata_present") for w in p.get("warnings", []))
    )
    pages_with_unrewritten_links = sum(
        1 for p in pages if any(str(w).startswith("unrewritten_confluence_links") for w in p.get("warnings", []))
    )
    summary = {
        "total_pages": len(pages),
        "source_pages": len(src_pages),
        "translated_pages": len(zh_pages),
        "static_pass": sum(1 for p in pages if p["static_status"] == "pass"),
        "static_fail": sum(1 for p in pages if p["static_status"] != "pass"),
        "browser_sampled_pass": sum(1 for p in pages if p["browser_visual_status"] == "passed_sample"),
        "browser_visual_pending": sum(1 for p in pages if p["browser_visual_status"] == "pending"),
        "pages_with_download_metadata": pages_with_download_metadata,
        "pages_with_unrewritten_confluence_links": pages_with_unrewritten_links,
        "known_static_offline_differences": [
            "Official site uses dynamic Refined/Confluence page tree; local docs use static manifest order.",
            "Official site search is dynamic; local docs use generated offline title/path/body index.",
            "Official homepage video is a static local preview.",
            "Downloader source/download metadata remains in HTML files but is hidden from the rendered reader view.",
        ],
    }
    report = {"summary": summary, "pages": pages}
    OUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(report)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
