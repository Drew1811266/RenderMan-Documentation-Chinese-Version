#!/usr/bin/env python3
"""Terminology audit helpers for the RenderMan Chinese documentation.

The script is intentionally non-destructive: it writes audit artifacts under
renderman-docs-27/terminology-audit and never edits translated HTML.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import html
import json
import re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC_ROOT = ROOT / "renderman-docs-27"
AUDIT_DIR = DOC_ROOT / "terminology-audit"
CANDIDATE_PATH = AUDIT_DIR / "overpreserve-candidates.tsv"
GLOSSARY_PATH = DOC_ROOT / "glossary" / "renderman_terminology.json"
HTML_ZH_ROOT = DOC_ROOT / "html-zh"

SKIP_TAGS = {
    "script",
    "style",
    "pre",
    "code",
    "kbd",
    "samp",
    "var",
    "svg",
    "math",
    "textarea",
    "noscript",
}
BLOCK_TAGS = {
    "p",
    "li",
    "td",
    "th",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "figcaption",
    "blockquote",
    "div",
}

PROTECTED_PATTERNS = [
    r"https?://[^\s\"'<>，。)）]+",
    r"(?:/Tractor|/blade)[^\s\"'<>，。)）]+",
    r"\b(?:ENGINE|BLADE|SSS|BBB|NNN|NAME|UUUU|CCCCC|XXX|sss|NNNN|CCCC|ATTRNAME)\b",
    r"\b(?:tsid|jid|tid|cid|nimby|owner|filter|metadata|fmt|qlen|full|probe|stats|statslog|subscribe|queue|monitor|ctrl|config|btrack|blade|q|set_[A-Za-z_]+|jretire|jrestore|jretry|ejectall|tskip|jrestart|jinterrupt|jattr|cattr|users|jobs|jtree|taskdetails|tasklogs|filters|getfilter|putfilter|getpreference|putpreference|delpreference|getsession|putsession|delsession|filterrules|reconfigure|status|limits|crewdetails|enumtierlist|mboxes|tracer|delist|loglevel|dbreconnect|blades|bdetails|battribute|statistics)\b",
    r'"[^"]+"',
    r"“[^”]+”",
    r"‘[^’]+’",
    r"\bPxr[A-Za-z0-9_]*\b",
    r"\bRix[A-Za-z0-9_]*\b",
    r"\bRi:[A-Za-z0-9_:.-]+\b",
    r"\bRf[MHKB]\b",
    r"\bRMAN[A-Z0-9_]*\b",
    r"\bPRMan\b",
    r"\bRenderMan(?:\s+(?:RIS|XPU|27|for\s+(?:Maya|Houdini|Katana|Blender)))?\b",
    r"\b(?:RIS|XPU|AOVs?|LPEs?|OSL|USD|OpenUSD|Alembic|OpenEXR|EXR|OpenVDB|OCIO|OpenColorIO)\b",
    r"\b(?:CPU|GPU|CUDA|DCC|API|JSON|XML|RIB|RLF|BSDF|BRDF|BxDF|Bxdf|GGX|UDIM|HDRI)\b",
    r"`[^`]+`",
    r"'[^']+'",
    r"\b(?:Maya|Houdini|Katana|Blender|Nuke|Solaris|MaterialX|Lama|Tractor|Pixar|Disney|SideFX)\b",
    r"\b(?:Pixar\s+Animation\s+Studios|Industrial\s+Light\s+&\s+Magic|Early\s+Access)\b",
    r"\b(?:Cookies\s+&\s+Milk|Louise|Crocostrich|Fridge|The\s+Walking\s+Teapot|Onward\s+Walking\s+Teapot|The\s+Hidden\s+People|Stirling|Stylized\s+Shipshape|Shipshape|9\s+to\s+3\s+Animation)\b",
    r"\b(?:Harsh\s+Agrawal|Leif\s+Pedersen|Eisko|Cronobo\s+Nexture|Victor\s+Besseau|Fabio\s+Sciedlarczyk|Dylan\s+Sisson|Luke\s+Cutler|Ernst\s+Janssen\s+Groesbeek|Ian\s+McQue|Ruslan\s+Safarov|Cheyenne\s+Chapel|Aliya\s+Chen|Damian\s+Kwiatkowski|Alyssa\s+Minko|Anthony\s+Muscarella|Miguel\s+Zozaya)\b",
    r"\b(?:Maya\s+Instances|RenderMan\s+Archive|Multiple\s+Materials|Particle\s+Instancer|XGen\s+Archives|Nested\s+Instancing|XGen\s+Description|Create\s+XGen\s+Description|XGen\s+Archive|Create\s+XGen\s+Archive|Specify\s+Points|Add\s+a\s+Material)\b",
    r"\b(?:HyperGraph\s+Hierarchy|Windows->HyperGraph:\s+Hierarchy|Modify->Freeze\s+Transformations|nParticle\s+Tool|nParticles->Instancer|XGen\s+Window|XGen\s+Primitives|Primitives|Archive\s+Files|Create\s+New\s+Description|Create\s+From\s+Selection|Export\s+Selection\s+as\s+Archives|Generate\s+Primitives|Randomly\s+across\s+the\s+surface|At\s+specified\s+locations|Preview/Output|RenderMan\s+Settings)\b",
    r"\b(?:RenderMan\s+Shelf|RenderMan\s+Menu|Hypershade(?:\s+Window)?|Light\s+Data|Gobo|Cookie|constant\s+Bxdf|glow|emission)\b",
    r"\b(?:Supported\s+Maya\s+Nodes|Hypershade\s+Nodes|2D\s+Textures|3D\s+Textures|Env\s+Textures|Other\s+Textures|Image\s+Planes|3D\s+Maya\s+Fluids|2D\s+Maya\s+Fluids)\b",
    r"(?:Surface（表面）|RenderMan\s+shading（RenderMan\s+着色）|Volumetric（体积）|RenderMan\s+volume（RenderMan\s+体积）|Displacement（位移）|displacement（位移）|Bulge（凸起）|Checker（棋盘格）|Cloth（布料）|File（文件）|Fluid\s+Texture\s+2D（2D\s+流体纹理）|Fractal（分形）|Grid（网格）|Mandelbrot（Mandelbrot\s+图案）|Mountain（山脉）|Movie（影片）|Noise（噪声）|Ocean（海洋）|PSD\s+File（PSD\s+文件）|Substance（Substance\s+材质）|Substance\s+Output（Substance\s+输出）|Water（水）|Brownian（布朗）|Cloud（云）|Crater（陨坑）|Fluid\s+Texture\s+3D（3D\s+流体纹理）|Granite（花岗岩）|Mandelbrot\s+3D（Mandelbrot\s+3D\s+图案）|Volume\s+Noise（体积噪声）|Layered\s+Texture（分层纹理）|Lights（灯光）|lights（灯光）|Image\s+Plane（图像平面）|Bifrost（Bifrost\s+模拟）)",
    r"\b(?:Object\s+Properties|Render\s+Properties|Render\s+Holdouts|Hold-Out|In\s+Alpha|Separate\s+AOV|Separate|adapt\s+all|traceholdout|holdouts|over)\b",
    r"\b(?:Node\s+Graph|Graph|Color\s+(?:tab|选项卡)|Nuke\s+Default|Life|Shift|Bezier|B-spline|roto\s+paint|png)\b",
    r"\b(?:Option|Options|Attribute|DisplayChannel|Hider)\b",
    r"(?<![-A-Za-z0-9_])(?:string|int|float|vector|color|normal|point)(?![-A-Za-z0-9_])",
    r"\b(?:primvar|primvars|primstr|txmake|maketx|stportal|hdPrman|prman|gpuCache|udim|tex|ptex|ptexturemaxfiles|atlas|alpha|dsominmax|singlescatter)\b",
    r"\b(?:hider|integrator|integrators|sampleoffset|sampleoffsets|samplestride|maxsamples|minsamples|bakeudimstride|bakeudimoffset|udim|udims|scenegraph|traversal|renderboot)\b",
    r"\b(?:getattribute|getmessage|trace|texture|texture3d|dsview|sho|debug|Read|ReadRegion|Write|Ci)\b",
    r"\b(?:Live\s+Stats|JSON\s+Report|Custom\s+Output|Primary\s+Hit|Primary\s+Hit\s+only|Line\s+Detect|Line\s+Generation\s+Modes|Variance\s+Line|Curvature\s+Thin\s+Line|Sobel\s+Map|Painterly\s+Brush|Geometry\s+Light|Light\s+Linking|RenderMan\s+Render\s+Settings|RenderMan\s+Render\s+Vars|Bucket\s+Order|World\s+Origin|Display\s+Filter|Sample\s+Filter|Deep\s+OpenEXR|Stylized\s+Looks|XPU\s+Features\s+and\s+Limitations|VFX\s+Reference\s+Platform|Texture\s+Manager|Preset\s+Browser|Attribute\s+Editor|Render\s+Stats|Camera\s+Visibility|Transmission\s+Visibility|Indirect\s+Visibility|indirect\s+visibility|Dicing\s+Projection|dicing\s+projection)\b",
    r"\b(?:Stylized\s+Hatching|Stylized\s+Lines|Toon\s+&\s+Lines|Hatching\s+On\s+Color|Hatch\s+On\s+Color|Hatch\s+On\s+Background|Add\s+Spec|Hatching\s+Comp|Hatching\s+Blend|Signal\s+Luminance|Signal\s+Energy|Triplanar\s+Test\s+Colors|Input\s+Page|Camera\s+Range\s+Page|Camera\s+Range\s+Mask\s+Switch|Z\s+Depth\s+Mode|Cam\s+Dist\s+Z\s+Min|Cam\s+Dist\s+Z\s+Max|Remap\s+Spline\s+Swatch\s+Select|Flip\s+Min\s+Max|Flip\s+Min\s+with\s+Max|Z\s+Min\s+Hatch\s+Frequency|Z\s+Max\s+Hatch\s+Frequency|Input\s+Remap\s+Page|Enable\s+Ramp|Hatching\s+Projection\s+Page|Triplanar\s+Projection|Triplanar\s+Blending|Hatching\s+Freq\s+Tex\s+1\s+-\s+Tex\s+8|Hatch\s+Tex\s+Color\s+Mix|Hatching\s+Color\s+Page|Hatching\s+Canvas\s+Page|Canvas\s+Color|Canvas\s+Texture|Hatching\s+Textures\s+Page|Texture\s+Set|Toon\s+Mode|Blending\s+Page|Color\s+Blend\s+Signal|First\s+Texture\s+is\s+White|Last\s+Texture\s+is\s+Black|Output\s+Page|Mask\s+Page|Light\s+Mask\s+Switch|Alpha\s+Hatch\s+Switch|NPR\s+Mix|Compositing\s+Page|Hatching\s+Tips)\b",
    r"\b(?:Final\s+Lines\s+Comp|Final\s+Lines\s+Invert|Final\s+Lines\s+Alpha|Final\s+Lines|Line\s+Thickness\s+from\s+PxrStylizedControl|Line\s+Thickness\s+from\s+Lighting|Line\s+Thickness\s+From\s+Lighting|Line\s+Detection\s+Page|Write\s+To\s+Type\s+AOV|Line\s+Thickness\s+Page|Line\s+Thickness\s+Remap\s+Page|Line\s+Thickness\s+Input|Line\s+Thickness|PxrStylizedControl\s+Scale|Z\s+Min\s+Thickness\s+Scale|Z\s+Max\s+Thickness\s+Scale|Dilation\s+Sorting\s+Page|Depth\s+Scale|Use\s+Alpha|Max\s+Depth|Line\s+Color\s+Page|Line\s+Color\s+Shadow|Line\s+Color|Color\s+Swatch|Light\s+Tint|HSV\s+Light\s+Dark|Line\s+Distort\s+Page|Line\s+Distort|Demo\s+videos|PxrStylizedControl\s+Mask|Input\s+Mask|Final\s+Line\s+Gamma|Lines\s+Inside\s+Alpha|Linework\s+Tips|Weight\s+Type|Double\s+Sigmoid|Dilate\s+Sort)\b",
    r"\b(?:Enable\s+Stylized\s+Looks|Attach\s+Stylized\s+Pattern|Attach\s+Stylized\s+Display\s+Filters|Stylized\s+Looks\s+Display\s+Filters|Combine\s+Display\s+Filters\s+to\s+really\s+get\s+creative|Display\s+Filters|Display\s+Filter|Stylized\s+shelf\s+button|Render\s+Settings|Stylized\s+AOVs?|Stylized\s+Rendering|View\s+AOVs?|Output\s+AOVs?|RenderMan\s+preferences|AOV\s+Output|Utility\s+Pattern|Stylized\s+Looks\s+Tip|Add\s+lighting|Interactive\s+Rendering)\b",
    r"(?:Render（渲染）|Threads（线程）|Rendering\s+Threads（渲染线程）|Batch\s+Threads（批量线程）|IPR\s+Display（IPR\s+显示）|Render\s+To（渲染到）|Output\s+AOVs（输出\s+AOVs）|Prune\s+Invisible\s+Nodes（裁剪不可见节点）|Batch\s+Render（批量渲染）|Spool\s+To（派发到）|Spool\s+Style（派发方式）|Frames\s+Per\s+Server（每台服务器帧数）|Checkpoint（检查点）|Launch\s+Denoiser（启动降噪器）|Start\s+Paused（暂停启动）|Priority（优先级）|Service（服务）|Env\s+Keys（环境键）|After（之后）|Crews（团队）|Tier（层级）|Scheduling\s+Modes（调度模式）|Projects（项目）|Comments（注释）|Metadata（元数据）|When\s+Done（完成时）|When\s+Error（出错时）|When\s+Always（总是执行）|Number\s+of\s+Processes（进程数量）|Fallback\s+Texture\s+Path（后备纹理路径）|Show\s+Advanced\s+Options（显示高级选项）|Texture\s+Extensions（纹理扩展名）)",
    r"(?<![-A-Za-z0-9_])(?:rfm-\*|maya-\*|rmantree=\*|rfmtree=\*|rmantree=\$RMANTREE|rfmtree=\$RFMTREE)(?![-A-Za-z0-9_])",
    r"\b(?:Input/Signal|Light\s+Signal\s+Range|Camdist\s+Range|Lighting\s+signal|line\s+distort\s+signal|light\s+Signal\s+color\s+AOV|light\s+AOV|1\s+value|8\s+values|Mode\s+=\s+8\s+values|Standard|Custom|Individual|Result|Disable|Final|Mask|Range|Input|Min|Max|Ramp|Node|Blending|Lines|Alpha|Type|Weight|From|Mult|Remap|Scale|Distort|Activation|Radius|Multiply|Over|Plus)\b",
    r"(?<![-A-Za-z0-9_])(?:triplanar|spline|ramp|customname|customname-|val|Hold|Bell|Curve|Coords)(?![-A-Za-z0-9_])",
    r"\b(?:base\s+color|albedo\s+color|Camera\s+Range|Hatching\s+Node|Stylized\s+Looks|Stylized\s+shaders|Bell\s+Curve|Canvas\s+mode)\b",
    r"\b(?:Signal|Frequency|Triplanar|Visualizer|Linstep|Swatch|Camdist|LineNZ|Sections|Outline|Curvature|Hermite|Sigmoid|NPRhatchOut|NPRPtriplanar|NPRNtriplanar|NPRtextureCoords|NPRalbedo|NPRP|NPRN|Canvas|Mix|Weighted|Overlap|GREEN|RED|ORANGE|YELLOW|BLUE|INDIGO|VIOLET|TURQUOISE|tex[1-8]|aov|AOV)\b",
    r"\b(?:Advanced\s+Tab|Render\s+Options|Output\s+All\s+Shaders|Reentrant\s+Procedural|Output\s+Holdout\s+Matte|Enable\s+Image\s+Plane\s+Filter|Learn\s+Light\s+Results|Bucket\s+Order|Bucket\s+Size|Opacity\s+Threshold|Reference\s+Frame|Adaptive\s+Sampler|Adaptive\s+Metric|Adapt\s+All|Micropolygon\s+Lenth|Watertight\s+Dicing|Dicing\s+Camera|Reference\s+Camera|Min\s+Hair\s+Width|Trace\s+Auto\s+Bias|Trace\s+Bias|Trace\s+World\s+Origin|Enable\s+Batched\s+OSL|OSL\s+Verbosity|OSL\s+Statistics\s+Level|Deep\s+Rendering|Crop\s+Window|Top\s+Left/Bottom\s+Right|IES\s+Profiles|Scene\s+units\s+to\s+meters|Ignore\s+Watts|Cache\s+Sizes|XML\s+File|LPE\s+Lobe\s+Mappings|Light\s+Path\s+Expression|User\s+Lobes)\b",
    r"\b(?:EnvDayLight|Daylight|Parameters|Intensity|Exposure|Direction|Haziness|Sky\s+Tint|Sun\s+Tint|Sun\s+Size|Ground\s+Mode|Legacy\s+Mode|Horizon\s+Clamping|Diffuse\s+Ground|Ground\s+Color|Month|Day|Year|Hour|Zone|Latitude|Longitude|Refine|Specular\s+Amount|Diffuse\s+Amount|Shadows|Enable\s+Shadows|Shadow\s+Color|Shadow\s+Max\s+Distance|Shadow\s+Falloff(?:\s+Gamma)?|Trace\s+Subset|Don't\s+Trace\s+Subset|Trace\s+Light\s+Paths|Thin\s+Shadows?|Visible\s+in\s+Refraction|Manifold\s+Walk(?:\s+Exclude\s+Group)?|Enable\s+Manifold\s+Walk|Light\s+Samples|Light\s+Group|Importance\s+Multiplier|Presets|Advanced|use\s+direction)\b",
    r"\b(?:Display\s+Format|Instance\s+Attributes|Op\s+Chain|Geolib|Ndsp|Reves)\b",
    r"\b(?:identifier:name|dice:minlength|polygon:smoothnormals)\b",
    r"\b(?:LamaLayer|LamaDielectric|LamaDiffuse|Material\s+Top|Material\s+Base|Top\s+Mix|Top\s+Thickness|Layer\s+Mode|Layering\s+Modes|Fresnel\s+Blend|Smooth\s+Coating|Rough\s+Coating|Relative\s+IOR|Clearcoat|absorptionColor)\b",
    r"\b(?:PxrLayerMixer|PxrLayerSurface|Layer\s+1|Input\s+Material|Copper/Bronze|Diffuse|Primary\s+Specular|Bias\s+Normal|Red\s+result)\b",
    r"\b(?:pxrMaterialOut|inputMaterial)\b",
    r"\b(?:Diffuse\s+Parameters|Specular\s+Parameters|Rough\s+Specular|Clear\s+Coat\s+Parameters|Iridescence\s+Parameters|Fuzz\s+Parameters|Subsurface\s+Scattering\s+Parameters|Single\s+Scattering\s+Parameters|Glow\s+Parameters|Glass\s+Parameters|Global\s+Properties\s+Parameters|Properties\s+Parameters|Input\s+Material|Diffuse\s+Color|Back\s+Color|Use\s+Diffuse\s+Color|Transmit\s+Gain|Transmit\s+Color|Double\s+Sided|Face\s+Color|Edge\s+Color|Artistic\s+Mode|Physical\s+Mode|Refractive\s+Index|Extinction\s+Coefficient|Fresnel\s+Exponent|Shading\s+Tangent|Layer\s+Thickness|Absorption\s+Tint|Primary\s+Color|Secondary\s+Color|Cone\s+Angle|Mean\s+Free\s+Path\s+Distance|Mean\s+Free\s+Path\s+Color|Multiple\s+Mean\s+Free\s+Paths|Post\s+Tint|Short\s+Gain|Short\s+Color|Long\s+Gain|Long\s+Color|Short\s+MFP\s+Distance|Long\s+MFP\s+Distance|Single\s+Scatter|Single\s+Scattering|Mean\s+Free\s+Path|Backside\s+Direct\s+Illum\s+Gain|Direction\s+Tint|Refraction\s+Gain|Reflection\s+Gain|Refraction\s+Color|Thin\s+Shadows|Unit\s+Length|Irradiance\s+Tint)\b",
    r"\b(?:Specular\s+Fresnel\s+Mode|Specular\s+Model|Specular\s+Clearcoat\s+Globals|Specular\s+Energy\s+Compensation|Clearcoat\s+Energy\s+Compensation|Iridescence\s+Mode|Falloff\s+Speed|Falloff\s+Scale|Flip\s+Hue\s+Direction|Subsurface\s+Model|Trace\s+Control|Consider\s+Backside|Continuation\s+Ray\s+Mode|Max\s+Continuation\s+Hits|Follow\s+Topology|Trace\s+Subset|Direct\s+Gain\s+Mode|Scattering\s+Globals|Irradiance\s+Roughness|Interior\s+Parameters|Single\s+Scatter\s+Albedo|Overlapping\s+Volumes|Multiscatter|Single\s+Directionality|Presence\s+Cached|Shadow\s+Mode|Shadow\s+Color|Utility\s+Pattern|All\s+Hits|Last\s+Hit|First\s+Hit|Shader\s+and\s+shadow\s+color|Shadow\s+color\s+only|per\s+micropolygon|per\s+shading\s+point|Clear\s+Coat|Specular\s+Fresnel|Jensen\s+Dipole|d'Eon\s+Better\s+Dipole|Burley\s+Normalized|Exponential\s+Path\s+Traced|Non-Exponential\s+Path\s+Traced|Path\s+Traced|3D\s+Manifold)\b",
    r"\b(?:Path\s+Guiding|Indirect\s+Guiding|PPG\s+Indirect\s+Guiding|RIS\s+Indirect\s+Guiding|Manifold\s+Walk|Manifold\s+Next\s+Event\s+Estimation|Russian\s+Roulette|Practical\s+Path\s+Guiding\s+for\s+Efficient\s+Light-Transport\s+Simulation|Trace\s+Light\s+Paths|Photon\s+Controls|Reference\s+(?:Position|Normal|World\s+Position|World\s+Normal)\s+primvar|Reference\s+Position|Reference\s+Normal|Reference\s+World\s+Position|Reference\s+World\s+Normal)\b",
    r"\b(?:Displacement\s+Space|Displacement\s+Types|Input\s+Parameters|Displacement\s+Bounds|Scalar\s+Displacement|Vector\s+Displacement|Model\s+Displacement|Micropolygon\s+Length)\b",
    r"\b(?:Displacement\s+Type|Vector\s+Space|Displacement\s+Height|Displacement\s+Depth|Remapping\s+Mode|Displacement\s+Center|Displacement\s+Scale\s+Space|Use\s+Displacement\s+Direction|Displacement\s+Direction(?:\s+Space)?|Default\s+Float|Generic\s+Vector|Mudbox\s+Vector|Z[Bb]rush\s+Vector|Absolute\s+Tangent|Relative\s+Tangent|Interpolate\s+Depth\s+and\s+Height)\b",
    r"(?<![-A-Za-z0-9_])(?:connect|merge|fireflies|developer|option|spatial|lookup|tree|Photons|photons|photon|world-space)(?![-A-Za-z0-9_])",
    r"\b(?:Texturing\s+Hair|Hair\s+Generator|Primitive\s+Variable|Hair\s+and\s+Fur\s+Presets|Download\s+Presets|Classic\s+Xgen\s+Example|Interactive\s+Grooming\s+Example|Diffuse\s+Gain|Primary\s+Specular|Secondary\s+Specular|Transmit\s+Specular|Specular\s+Gain|Primary\s+Specular\s+Gain|Secondary\s+Specular\s+Gain|Transmit\s+Specular\s+Gain|Glint\s+Gain|Primary\s+Specular\s+Color|Secondary\s+Specular\s+Color|Transmit\s+Specular\s+Color|Primary\s+Cone\s+Angle|Secondary\s+Cone\s+Angle|Transmit\s+Cone\s+Angle|Specular\s+Offset|Fresnel\s+Mix|Glint\s+Width|Eccentricity\s+Direction|Named\s+Lobes|Named\s+Diffuse\s+Lobe|Named\s+Specular\s+Lobes|User\s+Lobes|Zinke|Kajiya|Marschner|Xgen|Yeti|Glints|TRT|TT)\b",
    r"\b(?:Enable|Gain|Color|Roughness|Bump|Anisotropy|Thickness|Tint|Directionality|Blur|Presence|Normal|Diffuse|Specular|Subsurface|Iridescence|Fuzz|Glow|Glass|Refraction|Reflection|Clearcoat|Artistic|Physical|Pattern|Exponent|Extinction|Albedo|Off|On|Beckmann|GGX|Lambertian|Oren-Nayar|Marschner|Holographic)\b",
    r"\b(?:txmake|Wrap\s+Mode|Image\s+Resize|Resize\s+Filter|Image\s+Blur|Bleed\s+Alpha|Mipmap\s+Pattern|Mipmap\s+Source|User\s+Mipmaps|Mipmap\s+Filter|Environment\s+Map|Lat-Long\s+Map|Diffuse\s+Convolution|Cube\s+Map|Ptex\s+Cube\s+Map|Spherical\s+Harmonic\s+Bands|Image\s+Format|Data\s+Compression|Data\s+Type|Display\s+Window|Bump\s+To\s+Roughness|Shadow\s+Map|Min/Max\s+Shadow\s+Map|Pyramid\s+Shadow\s+Maps|Command\s+Line|Directory\s+Map)\b",
    r"\b(?:OCIO\s+Roles|JSON\s+Configuration\s+file|File\s+name|File\s+location|Sample\s+file|Roles/ColorSpaces|Texture\s+Manager|conversion\s+defaults|node\s+types|args\s+dict|rendering\s+role|ACES\s+colorspace|luma\s+coefficients|basic\s+linear|Filmic-Blender|Utility\s+-\s+sRGB\s+-\s+Texture)\b",
    r"(?<![-A-Za-z0-9_])(?:texture_type|texture_format|texture_filter|data_type|compression_level|ociocolorspace|ocioconvert|ociodither|bumprough|mipfilter|node_type|classification|img_name|img_ext|img_atlas|img_type|img_depth|img_nchan|ocioconfig|ocioconfig_name|True|False|null|imageplane)(?![-A-Za-z0-9_])",
    r"\b(?:Constant\s+fog|Smoke|Fire|Clouds|Crepuscular\s+Beams|Moana\s+Cloud|Walt\s+Disney\s+Animation|CC\s+BY-SA)\b",
    r"\b(?:Diffuse\s+Color|Emit\s+Color|Light\s+Source|Multiple\s+Scattering|Velocity\s+and\s+Motion\s+Blur|Density\s+Parameters|Density\s+Float\s+PrimVar|Density\s+Float|Density\s+Color\s+PrimVar|Density\s+Color|Max\s+Density|Anisotropy\s+Parameters|Primary\s+Anisotropy|Secondary\s+Anisotropy(?:\s+and\s+Lobe\s+Blend\s+Factor)?|Sampling\s+Parameters|Equiangular\s+Weight|min/max\s+Samples|Multiscatter\s+Optimization|Extinction\s+Multiplier|Contribution\s+Multiplier|Velocity\s+Multiplier|Using\s+Meshlight|User\s+Lobes)\b",
    r"\b(?:Volume\s+Scattering\s+Approximation|Max\s+Path\s+Length|Density\s+Scale|Lobe\s+Blend(?:\s+Factor)?|Primary\s+lobe|Secondary\s+lobe|Aggregate\s+Membership|Volume\s+Aggregate\s+Name|Default\s+Ray\s+Depth|Max\s+Specular\s+Depth|Max\s+Diffuse\s+Depth|Max\s+Indirect\s+Bounces|PxrPathTracer\s+Parameters)\b",
    r"(?<![-A-Za-z0-9_])(?:Gain|Bleed|Contribution|Blend|Primary|Secondary)(?![-A-Za-z0-9_])",
    r"\b(?:Source\s+Intensity\s+Scale|Intensity\s+Volume|Flame\s+Volume|Diffuse\s+Color\s+Ramp|Color\s+Intensity\s+Scale|Scatter\s+Color\s+Ramp|Diffuse\s+Masking|Enable\s+Mask|Fire\s+Volume\s+Mask\s+Scale|Fire\s+Volume\s+Mask\s+Intensity\s+Ramp|Fire\s+Volume\s+Mask|Emission\s+Color|Emission\s+Masking|Source\s+Volume\s+Intensity\s+Ramp|Destination\s+Range|Bindings|Flame|Scatter)\b",
    r"\b(?:RenderMan\s+Volume|Box\s+Parameters|Voxel\s+Resolution|VDB\s+Parameters|Density\s+Grid|Density\s+Multiplier|Density\s+Rolloff|Filter\s+Width|Box\s+Volumes|OpenVDB\s+Volumes|OpenVDB\s+Shading\s+Network|OpenVDB\s+Fire|Density\s+bias|Incandescence|Filename|Blobbies)\b",
    r"(?<![-A-Za-z0-9_])(?:box|vdb|uniform|non-uniform|rolloff|mipmapping|mipmap|incandescence)(?![-A-Za-z0-9_])",
    r"\bPrmanVolume\s+type\b",
    r"(?<![-A-Za-z0-9_])(?:density|densityFloat|densityColor|max\s+density|density\s+float|density\s+color|equiangular\s+weight|primary\s+anisotropy|secondary\s+anisotropy|anisotropic\s+lobe|lobe|mesh\s+light|emission|velocity|albedo)(?![-A-Za-z0-9_])",
    r"\b(?:Image\s+Tool|Image\s+Window|Sequence\s+Controls|Monitor\s+Controls|Pixel\s+Readout|Preferences\s+Window|Display\s+Mapping|AI\s+Denoise|Recent\s+Bucket\s+Markers|Color\s+chart\s+generator|Analysis\s+Tools|Custom\s+Display\s+Range|Isolate\s+Values|Dump\s+Metadata\s+to\s+message\s+log|Custom\s+View|Custom\s+Views|Burn\s+Mapping(?:\s+On\s+Save)?|Image\s+Cache\s+Size|Scratch\s+Image\s+Location|Short\s+Window\s+Titles|Focus\s+Incoming\s+Render|Automatic\s+view\s+mapping|Shadow\s+Map|File->New\s+Catalog|Image->Toggle\s+Background|View->Lock\s+Pixel\s+Readout|File->Open\s+Sequence|File->Open\s+Image|Nvidia\s+AI\s+Denoiser|Optix\s+Denoiser|Importance\s+Sample\s+Filtering|Importance\s+Sample\s+Filter)\b",
    r"\b(?:Pan\s+Tool|Zoom\s+Tool|Crop\s+Tool|Scrub\s+Tool|Wipe\s+Tool|Select\s+Object\s+Tool|Select\s+Surface\s+Tool|Reset\s+Zoom|Cancel\s+Render|Play\s+Sequence|Loop\s+Mode|Step\s+Back\s+Frame|Step\s+Forward\s+Frame|Exposure\s+Up\s+1\s+F-Stop|Exposure\s+Down\s+1\s+F-Stop|Gamma\s+Up\s+0\.1|Gamma\s+Down\s+0\.1|New\s+bucket\s+indicator|Nvidia\s+AI\s+Denoising|No\s+AOVs)\b",
    r"\b(?:Nvidia|NVIDIA|Kepler|Maxwell|Optix|OptiX|Denoiser|denoiser|Ctrl|Cmd|Ctrl/Cmd|PageUp|PageDown|F-Stop|8-bit|16-bit|Float|beauty|Beauty|bucket|qss)\b",
    r"\b(?:Cryptomatte|Apple\s+Silicon|Lookdev|Open\s+Shading\s+Language|Deep\s+IDs?|OpenEXR\s+Deep\s+IDs?|Min\s+Width|deepidextract|deepidselect|Listener|Debug\s+Logging|Package\s+Scene|Join\s+Geometry|refresh\s+IPR|XPU\s+Preview|Scene\s+Import|Vertical\s+Sweep|Render\s+Gallery|RenderSettings|PxrOptionsAPI|HdPrmanLoaderRendererPlugin_Global\.ds)\b",
    r"\b(?:Normal\s+Map|Primary\s+Hit\s+only|Output\s+Line|Painterly\s+Brush|Custom\s+Tex|Size\s+Space|Screen\s+Space|Raw\s+Data|Timer|Memory|Counter|JSON\s+Report|Live\s+Stats|Frame\s+Range|UV\s+Tile|RenderMan\s+Standard\s+Render\s+Vars|RenderMan\s+Render\s+Vars)\b",
    r"\b(?:Pass|Passes|Arbitrary\s+Output\s+Variables|Render\s+Layers|Display\s+Channels?|Display\s+Drivers?|Display\s+Settings|Display\s+Type|As\s+RGBA|Deep\s+Data|Storage|Tiled|Planar|Half\s+Precision|Float\s+Precision|Compression\s+Level|Texture\s+Format|Bit\s+Depth|EXR\s+Bit\s+Depth|S\s+and\s+T\s+Wrap\s+Modes|EXR\s+Compression(?:\s+Level)?|Resolution\s+Unit|Display\s+Channel\s+Settings|Channel\s+Type|Channel\s+Source|LPE\s+Light\s+Group|Filter\s+Width|Statistics|Break\s+Point|Max\s+Value|Smoothness|Single\s+Frame|Cross-frame|Final\s+Pass|Data\s+AOVs?|Data\s+AOV|Z\s+depth|CPU\s+Time|Batch\s+Render)\b",
    r"\b(?:Channels?|Displays|Driver|Wiki|Tiff|Half|Byte|Short|Targa|Packbits|Deflate|Pixarlog|Lossless|Lossy|Matte|rgba|breakpoint|direct\s+diffuse|indirect\s+specular|deep\s+data|Volumes|periodic)\b",
    r"\b(?:Custom|Standard|Diagnostic|Lighting|Denoiser|Shadow|Mattes|Integrator)\s*:",
    r"(?<![-A-Za-z0-9_])(?:minwidth|lightfilter|excludesubset|shadows|invshadows|occluded|unoccluded|schema|schemas|stage|hbatch|husk|barn|cookie|bypass|resize|non-tiled|mipmapped)(?![-A-Za-z0-9_])",
    r"(?<![-A-Za-z0-9_])(?:Ptex|constant|string|Nearest|dmfp|Chiang|Bxdfs|intersectpriority|black|mirror|Pref|primitive|non-hexmode|zip|ini|lpe)(?![-A-Za-z0-9_])",
    r"\b(?:Catalog|Tools|Inspector|Snapshot|Views|Background|Remapping|Sequences|Palette|Denoise|Gamma|Exposure|Bucket|Buckets|Sequence|Window|Zoom|Readout|Mapping|Display\s+Range|Notes|Font|Classic|Hue|Linearize|OpenColorIO|RMS_SCRIPT_PATHS|OCIO)\b",
    r"\b(?:Intel|Intel®|Advanced\s+Vector\s+Extensions|Streaming\s+SIMD\s+Extensions|SIMD|AVX-512|AVX2|AVX|SSE4\.2|Batched|batched|OpenShadingLanguage|oslc|oso|osl|lockgeom|shadeop|rendererInfo|shadingMode|RixShadingContext|RixSCShadingMode|RixShading\.h)\b",
    r"\b(?:SEVERE|ERROR|MESSAGE|WARNING|INFO|presence|opacity|scatter|volumeTransmission|volumeScatter|emission|bake|displacement|eyePath|lightPath|primaryHit|missContext|reyesGrid)\b",
    r"\b(?:Gobo|Blocker|Cookie|Rod|Hatching|Toon|Triplanar|Screen|Screen\s+Space|Size\s+Space|Bump\s+Roughness|gaussian\s+refit|Rotation|Random|Degrees|Shading\s+Tangent|Normals|Tangent|Nref|Clearcoat|Geometry|Render|Shading|Settings|Projections|Normal|Line)\b",
    r"\b(?:Over|Multiply|Plus|Difference|Divide|Exclusion|Darken|Lighten|Overlay|Soft\s+Light|Hard\s+Light|Color\s+Dodge|Color\s+Burn|Linear\s+Dodge|Linear\s+Burn|Vivid\s+Light|Pin\s+Light|Enhanced\s+Difference)\b",
    r"\b(?:true|false|on|off|Auto|contrast|variance|halfbuffer|contrast-v22|variance-v22|weighted|importance|raytrace|bake|pattern|all|world|worldorigin|worldoffset|camera|dtex|exitat|Jensen|Brickmap|Rif)\b",
    r"\b(?:min\s+max|left\s+right\s+top\s+bottom)\b",
    r"\b(?:trim|blp|horizontal|vertical|zigzag-x|zigzag-y|spacefill|random|spiral|circle)\b",
    r"\b(?:inside|outside|viewfrustumdistance|worlddistance|objectdistance|planarprojection|instanceprojection|displacementbound|ImplicitField|BoxMotion|Eulerian)\b",
    r"\b(?:LOP|LOPs|ROP|COPs|VOP|VOPs|Husk)\b",
    r"\b(?:Render\s+in\s+Background|View\s+RIB|View\s+Rib|Valid\s+Frame\s+Range|Start/End/Inc|Render\s+With\s+Take|Override\s+Camera\s+Resolution|Enable\s+Depth\s+of\s+Field|Allow\s+Motion\s+Blur|Sampling\s+Tab|Adaptive\s+Metric|Exposure\s+Bracket|Dark\s+Falloff|Pixel\s+Variance|Interactive\s+Refinement|Minimum\s+Samples|Extra\s+Minimum\s+Samples|Maximum\s+Samples|Adapt\s+All|Pixel\s+Filter\s+Mode|Sample\s+Offset|Extreme\s+Motion/DOF|Default\s+Ray\s+Depth|World\s+Origin|World\s+Offset|Light\s+Learning\s+Scheme|Checkpoint\s+Render|Search\s+Paths|Shader\s+Path|Texture\s+Path|Display\s+Path|Archive\s+Path|Procedural\s+Path|Rix\s+Plugin\s+Path|Directory\s+Map|Minimum\s+Width|Offscreen\s+Multiplier|Render\s+Statistics|Bucket\s+Order|Order\s+Origin|Frame\s+Aspect|Variable\s+Substitution)\b",
    r"\b(?:Renderer\s+Options|Binary|sampleoffset|bucket/tile|bucket|tile|delayed\s+read\s+archives|fall\s+through|horizontal|vertical|zigzag-x|zigzag-y|spacefill|spiral|circle|Display\s+plugins?|shader\s+plugins?|procedural\s+plugins?)\b",
    r"\b(?:RenderMan\s+Geometry|Export\s+as\s+CoordSys|Plain\s+Axis|3D\s+Placement|Coordinate\s+System|Ramp\s+Type|T\s+Ramp|EmitColor|Multiply\s+ink\s+mode)\b",
    r"\b(?:Mari|Substance\s+Painter)\b",
    r"\b[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)+\b",
    r"\b(?:Blade|Engine|Dashboard)\b",
    r"\btractor-(?:engine|blade|spool|dbctl)\b",
    r"\btractor(?:[-.][A-Za-z0-9_]+)+\b",
    r"\b(?:ProfileDefaults|BladeProfiles|BladeProfile|ProfileName|Hosts|Access|Provides|Capacity|EnvKeys|SiteModulesPath|CmdOutputLogging|VersionPin|TaskBidTuning|TR_EXIT_STATUS_terminate|RecentErrorThrottle|DirMapZone|UDI|NIMBY|GPUExclusionPatterns)\b",
    r"\b(?:NimbyCrews|NimbyConnectPolicy|MaxSlots|MaxLoad|MinRAM|MinDisk|MinNCPU|MinPhysRAM|PhysRAM|MinNGPU|PathExists|Platform|NCPU|Name|Crews|GPU\.label)\b",
    r"\b(?:Project-A|Project-B|bob|pixarRender|pixarNRM|BigLinux|OtherLinux|Linux_machines|8core_rack|server_of_last_resort|factory|QXL|Standard\s+VGA)\b",
    r"(?<![-A-Za-z0-9_])(?:int|float|immediate|environment|envhandler|envhandlers|envkeys|keys|nimby|pinned)(?![-A-Za-z0-9_])",
    r"\b(?:CmdOutputLogging|SiteCmdLogServerStartup|SiteCmdLogRetrievalURL)\b",
    r"\b(?:logrotate|journald|SIGHUP|stdout|stderr|logfile|logserver|prman|i-node|compress|delaycompress|CORS|Apache|XHR|Web|UI|JSON|NFS|DFS|SMB|UNC)\b",
    r"\blogging\.(?:handlers\.RotatingFileHandler|configs\.fileConfig)\b",
    r"\b(?:filename|NNN|setuid|Alfred|System\s+Services|init\.d)\b",
    r"(?<![-A-Za-z0-9_])(?:Logs|Inline|local|print)(?![-A-Za-z0-9_])",
    r"\b(?:RemoteCmd|Cmd|Task|Tasks|Job|Instance|Assign|Iterate|JobEditAccessPolicies|PixarRender|EnvHandler)\b",
    r"\b(?:Cmds|RemoteCmds|RANGE|ITER|HOST|JOB_ID|JOB_OWNER|JID|LOGIN|PASSWD|CONFIGFILE|HADDR|MINSECS|MAXSECS|MAXSEC|TAGS|TTITLE|SVCKEY|CMDSVCKEY|ENVKEY|DIRNAME|PROJECTS|FLOAT|KEY|LIST|FILENAME)\b",
    r"\b(?:Hostname\[:port\]|host:port|jobfiles|chdir|spooling|print\s+spooling|shell\s+token|environment\s+packages|portability\s+aliases|Limit\s+Allocations|format\(\)|Error|None|INDEPENDENT|SINGLE)\b",
    r"\b(?:Not\s+In\s+My\s+Back\s+Yard|Always\s+allow\s+remote\s+commands|Private\s+use\s+for|Local\s+command\s+use\s+only\s+-\s+no\s+remote\s+jobs|Remote\s+Use\s+during\s+screen\s+saver\s+only|Remote\s+use\s+after\s+5\s+minutes\s+idle|Active\s+Jobs|Eject\s+Active\s+Jobs)\b",
    r"\b(?:Filter\s+Lister|Filter\s+Rule|Filter\s+Editor|Filter\s+Name|Any/All\s+Pulldown|First\s+Column\s+Pulldown|Spool\s+Time|Finish\s+Time)\b",
    r"\b(?:/Applications|Program\s+Files|tractor-blade-\$version|nimby\.bat|tractorconfig|passwd)\b",
    r"'(?:both|sfmt|text|min|max|min,max|min-max)'",
    r"\bred,green,blue\b",
    r"\bred\s+house,green\s+lawn,blue\s+sky\b",
    r"\bTheFilm\s+lighting\b",
    r"-(?:after|afterjids|atleast|atmost|service|envkey|postscript|when|whendone|whenerror|remotecleankeys|cmds|subtasks|serialsubtasks|resumeblock|resumewhile|chaser|cleanup|id|refersto|retryrc|by|from|to|template)\b",
    r"\b(?:envkey|setenv|resumewhile|resumeblock|serialsubtasks|postscript|expand|checkout|task-restart|netrender|atleast|atmost|varname|value_string|minrunsecs|maxrunsecs|min_servers|max_servers|appname|app_args)\b",
    r"\b(?:month|day|hour|minute|after|exitcode|testcheckpoint|TYPE|VALUE|OpenEXR)\b",
    r"\b(?:shared\s+servers|Task-level|multislot|checkpoint-resume|just-in-time)\b",
    r"\b(?:Limit\s+tag|Share\s+Names|launch\s+expression|parameter\s+substitution|task\s+descriptions|Task\s+descriptions|environment\s+handlers)\b",
    r"\b(?:shell|show|clean-up|shared|render|resume|Limit|Backslash|escape|limit-tags|pbias|wrangling|Administrators|zone|finally|chapters|prepare|phase|pipeline|footprint|binary)\b",
    r"(?<![-A-Za-z0-9_])(?:tag|env|app|title|image|descriptions)(?![-A-Za-z0-9_])",
    r"\b(?:Job|Task|Command)\.spool\(\)\b",
    r"\bEngineClient\.spool\(\)\b",
    r"\btractor\.api\.author\b",
    r"\b[A-Za-z]+[A-Z][A-Za-z0-9_]*\b",
    r"\b[A-Za-z0-9_.+-]+\.(?:config|conf|plist|ini|tex|ocio|webp|png|exr|rib|json|xml|py|cpp|h|osl)\b",
    r"\bconfig/\b",
    r"--[A-Za-z0-9_-]+",
    r"\bhttps?://\S+\b",
    r"\bwww\.[A-Za-z0-9_.-]+\b",
    r"\b(?:Windows|Linux|macOS|OSX|Mac\s+OS\s+X|Unix|Python|Tcl|JavaScript|PostgreSQL|SQLite|WebKit|CSS|HTTP|SQL)\b",
    r"\b(?:systemd|sysvinit|launchd|plist|nimby|NIMBY|metadata|refersto|rfm|envkeys|crews)\b",
    r"\b(?:postgresql|PostgreSQL|psql|cmdlogger|boilerplate|try-except|KeyboardInterrupt)\b",
    r"\brfm[-A-Za-z0-9]*\b",
    r"\brms-?\b",
    r"\bshared(?:\.[A-Za-z0-9*_-]+)+\b",
    r"\b[A-Za-z0-9_.+-]+\.file\b",
    r"\b/monitor\?q=jobs(?:&owner=\*)?\b",
    r"\bTractor/monitor\?q=statistics\b",
    r"\bTransaction\s+check\s+error:\s+file\s+/opt\s+from\s+install\b",
    r"\b(?:Job|Task|Command|RemoteCmd|Assign|Instance)\b",
    r"(?<![-A-Za-z0-9_])(?:ready|active|blocked|pending|done|error|kill|lock|spool|share|zero)(?![-A-Za-z0-9_])",
    r"(?<![-A-Za-z0-9_])(?:cap|nominal|reserved|clamp|project|allocation|decrement|increment)(?![-A-Za-z0-9_])",
    r"\b(?:Cmd\s+not\s+Ready|Cmd\s+not\s+Ready\?)\b",
    r"\b(?:Serial|Real|Thread|Sys|Activity)\s+Elapsed\b",
    r"\b(?:Elapsed|App\s+Secs|Sys\s+Secs|Thread\s+Elapsed|Activity\s+Span)\b",
    r"\b(?:Delete\s+Job|Archive\s+Job|Shuffle\s+Job\s+To\s+Top|Clear\s+(?:prior|earlier)\s+Blade\s+Data|quick\s+job\s+syntax\s+check)\b",
    r"\b(?:Task\s+Graph|Task\s+Info|Control-click|RenderMan\s+format|Alfred\s+format|chaser)\b",
    r"\b(?:Dispatching\s+Tiers|Job\s+Authoring\s+API|Privilege\s+Insulation|Resource\s+Usage\s+Tracking|Job\s+Spooling|Task\s+Elapsed\s+Time\s+Bounds|Per-Tier\s+Scheduling|Site-defined\s+Task\s+Log\s+Filters|GPU\s+Detection|Engine\s+statistics\s+query|Concurrent\s+Expand\s+Chunks|Cookie-based\s+Dashboard\s+relogin|Overall\s+Throughput\s+Optimizations|Archived\s+Jobs\s+View|User-centric\s+Job\s+Shuffle|Dashboard\s+Job\s+Pins|Dashboard\s+Job\s+Locks|Dashboard\s+Blade\s+Notes|Dashboard\s+Job\s+Notes)\b",
]

PRIORITY_PROTECTED_PATTERNS = [
    r"\bTransaction\s+check\s+error:\s+file\s+/opt\s+from\s+install\b",
    r"\bRenderMan\s+for\s+(?:Maya|Houdini|Katana|Blender)\b",
    r"\b(?:shared-access|partial-graph\s+looping|classic|non-checkpoint)\b",
    r"\b(?:run-time\s+bounds|no-retry\s+stop|time-bounds|retryrc)\b",
    r"\b(?:rush|default|admin|batch)\b",
    r"\bJSON\s+statistics\s+report\b",
    r"\b(?:Attributes\s+>\s+RenderMan\s+>\s+Visibility\s+Settings|Visibility\s+for\s+camera|Double-Sided\s+Transmit|Diffuse\s+controls)\b",
    r"(?:Box\s+Parameters（Box\s+参数）|Box\s+体积|PrmanVolume\s+type\s+参数|density\s+bias)",
    r"\bUse\s+World\s+Space\s+Radius\s+Units\b",
    r"Instance\s+Attributes（实例属性）",
    r"(?:Min\s+Width|Pixar\s+Animation\s+Studios|PxrMultiTexture\s+grid|grid\s+参数|Custom\s+Tex|Layer\s+图层合成模式|Layer\s+任意|shadow\s+LPE|offset、scale\s+和\s+rotation|internal\s+场景\s+ingestion|side-by-side|over-under)",
    r"(?:Object\s+Properties（对象属性）|Render\s+Properties（渲染属性）|Render\s+Holdouts|Hold-Out\s+设置为\s+Yes|adapt\s+all)",
]

COMMON_TRANSLATIONS = {
    "dicing projection": "细分投影",
    "intersection priority": "相交优先级",
    "cool colors": "冷色",
    "warm colors": "暖色",
    "shader object files": "着色器目标文件",
    "current space": "当前空间",
    "object space": "对象空间",
    "tangent space": "切线空间",
    "world space": "世界空间",
    "attribute namespace": "属性命名空间",
    "rest position": "静止位置",
    "user attribute": "用户属性",
    "user attributes": "用户属性",
    "transform node": "变换节点",
    "box filter": "盒式滤镜",
    "display filters": "显示滤镜",
    "bilinear patch": "双线性面片",
    "alpha channel": "Alpha 通道",
    "production integrators": "生产级积分器",
    "layer mask": "层遮罩",
    "portal lighting": "门户照明",
    "emission token": "发光标记",
    "cut out": "镂空",
    "attribute editor": "属性编辑器",
    "channel box": "通道盒",
    "pass-through node": "直通节点",
    "pattern nodes": "Pattern 节点",
    "texture nodes": "纹理节点",
    "shading network": "着色网络",
    "normal map color": "法线贴图颜色",
    "material closure": "材质闭包",
    "material closures": "材质闭包",
    "shader global": "着色器全局变量",
    "filter type": "滤镜类型",
    "normal pattern": "法线 pattern",
    "procedural noise": "程序化噪声",
    "bump nodes": "凹凸节点",
    "shader ball": "着色球",
    "texture primvars": "纹理 primvar",
    "trace groups": "追踪组",
    "camera rays": "相机光线",
    "indirect rays": "间接光线",
    "camera visibility": "相机可见性",
    "indirect visibility": "间接可见性",
    "shadow visibility": "阴影可见性",
    "transmission visibility": "透射可见性",
    "display channels": "显示通道",
    "raytrace hider": "光线追踪隐藏器",
    "indirect bounces": "间接反弹",
    "ray subsets": "光线子集",
    "trace memberships": "追踪成员关系",
    "trace sets": "追踪集",
    "global setting": "全局设置",
    "displacement shader": "置换着色器",
    "incandescence color": "自发光颜色",
    "scatter transmission": "散射透射",
    "object space": "对象空间",
    "random id": "随机 ID",
    "atlas textures": "图集纹理",
    "texture manifold": "纹理流形",
    "wrap mode": "包裹模式",
    "bridge tools": "桥接工具",
    "light visibility settings": "灯光可见性设置",
    "raster-oriented dicing": "面向栅格的细分",
    "scene units": "场景单位",
    "manifold utility": "流形工具节点",
    "atlas texture workflows": "图集纹理工作流",
    "baking workflow": "烘焙工作流",
}

RESIDUAL_WORD_TRANSLATIONS = {
    "job": "作业",
    "jobs": "作业",
    "task": "任务",
    "tasks": "任务",
    "command": "命令",
    "commands": "命令",
    "blade": "Blade（执行节点）",
    "blades": "Blade（执行节点）",
    "engine": "Engine（调度引擎）",
    "dashboard": "Dashboard（仪表板）",
    "file": "文件",
    "files": "文件",
    "config": "配置",
    "configuration": "配置",
    "server": "服务器",
    "service": "服务",
    "process": "进程",
    "script": "脚本",
    "scripts": "脚本",
    "node": "节点",
    "nodes": "节点",
    "texture": "纹理",
    "textures": "纹理",
    "pattern": "pattern/图案",
    "patterns": "pattern/图案",
    "light": "灯光",
    "lights": "灯光",
    "render": "渲染",
    "renderer": "渲染器",
    "rendering": "渲染",
    "geometry": "几何体",
    "scene": "场景",
    "filter": "滤镜",
    "filters": "滤镜",
    "image": "图像",
    "images": "图像",
    "material": "材质",
    "materials": "材质",
    "shader": "着色器",
    "shaders": "着色器",
    "shading": "着色",
    "attribute": "属性",
    "attributes": "属性",
    "camera": "相机",
    "map": "贴图",
    "maps": "贴图",
    "layer": "层",
    "layers": "层",
    "displacement": "置换",
    "diffuse": "漫反射",
    "specular": "镜面反射/高光",
    "sample": "采样/样本",
    "samples": "采样/样本",
    "sampling": "采样",
    "density": "密度",
    "user": "用户",
    "object": "对象",
    "objects": "对象",
    "volume": "体积",
    "volumes": "体积",
    "environment": "环境",
    "output": "输出",
    "outputs": "输出",
    "log": "日志",
    "key": "键",
    "keys": "键",
    "data": "数据",
    "host": "主机",
    "hosts": "主机",
    "lobe": "波瓣",
    "lobes": "波瓣",
    "instance": "实例",
    "instances": "实例",
    "option": "选项",
    "options": "选项",
    "value": "值",
    "values": "值",
    "name": "名称",
    "type": "类型",
    "default": "默认值",
    "description": "说明",
}

BILINGUAL_TRANSLATIONS = {
    "per-light AOVs": "逐灯光 AOV",
    "color AOV": "颜色 AOV",
    "float AOV": "浮点 AOV",
    "light group LPEs": "灯光组 LPE",
    "custom LPE": "自定义 LPE",
    "custom LPE expression": "自定义 LPE 表达式",
    "custom LPE name": "自定义 LPE 名称",
}

TITLE_TRANSLATIONS = {
    "Depth of Field": "景深",
    "Depth Of Field": "景深",
    "Layered Materials": "分层材质",
    "Presence and Opacity": "存在性与不透明度",
    "Stylized Hatching Sample XPU": "风格化排线示例 XPU",
    "Stylized Light Control": "风格化灯光控制",
    "Stylized Lines": "风格化线条",
    "Stylized Lines Control": "风格化线条控制",
    "Stylized Lines XPU": "风格化线条 XPU",
    "The Viewing Transformation": "观察变换",
    "Field of View": "视场角",
}

EXACT_DECISIONS = {
    "string name": ("preserve", "RIB/attribute declaration fragment"),
    "int id": ("preserve", "display channel declaration fragment"),
    "int maxsamples": ("preserve", "option declaration fragment"),
    "int wireframe": ("preserve", "parameter declaration fragment"),
    "string style": ("preserve", "parameter declaration fragment"),
    "constant string primvar": ("preserve", "primvar declaration fragment"),
    "constant float": ("preserve", "type declaration fragment"),
    "varying float": ("preserve", "type declaration fragment"),
    "rendermn.ini": ("preserve", "file name"),
    "stats.ini": ("preserve", "file name"),
    "texture.tex": ("preserve", "file name"),
    "foo.format": ("preserve", "placeholder file name"),
    "foo.tex": ("preserve", "placeholder file name"),
    "config.ocio": ("preserve", "file name"),
    "ultraman-docs.webp": ("preserve", "image asset file name"),
    "openvdb.org": ("preserve", "URL/domain"),
    "www.amaanakram.com": ("preserve", "URL/domain"),
    "s,t": ("preserve", "texture coordinate domain"),
    "-resize up": ("preserve", "txmake option"),
    "noclamp;prefix": ("preserve", "LPE prefix syntax"),
    "Attribute \"identifier\" \"float id\"": ("preserve", "RIB attribute syntax"),
    "Attribute \"identifier\" \"string name\"": ("preserve", "RIB attribute syntax"),
    "Attribute \"volume\" \"fps\"": ("preserve", "RIB attribute syntax"),
    "RIS builtin": ("preserve", "RenderMan API category"),
    "Renderman for Maya": ("preserve", "source spelling variant of product name"),
    "Industrial Light & Magic": ("preserve", "studio name"),
    "The Irishman": ("preserve", "film title"),
    "Material X Lama": ("preserve", "source spelling variant normalized elsewhere"),
    "Materials X Lama": ("preserve", "source spelling variant normalized elsewhere"),
    "Ou Color G": ("review-required", "source typo or shader output label"),
}

CONTEXT_UI_POS = {
    "option",
    "parameter",
    "section-title",
    "section",
    "ui-section",
    "ui-setting",
    "ui-attribute",
    "parameter-group",
    "parameter-heading",
    "parameter-label",
    "parameter-title",
    "option-label",
    "ui-label",
    "ui-parameter",
    "ui-parameter-group",
    "ui-value",
    "visualizer-mode",
    "enum",
    "mode",
    "mode-label",
    "dcc-ui",
    "maya-ui",
    "tool",
    "texture-map",
}

CONTEXT_TITLE_POS = {
    "page-title",
    "paper-title",
    "asset-title",
    "artist-credit",
    "credit",
    "film-title",
    "material-example",
    "example-scene",
    "workflow-title",
    "tip-title",
    "caption",
    "link-title",
}


class VisibleTextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.skip_depth = 0
        self.stack: list[str] = []
        self.current: list[str] = []
        self.chunks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        attr_map = {k.lower(): (v or "") for k, v in attrs}
        class_value = attr_map.get("class", "")
        if tag in SKIP_TAGS or "source" in class_value.split():
            self.skip_depth += 1
        self.stack.append(tag)
        if not self.skip_depth and tag in BLOCK_TAGS:
            self._flush()

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if not self.skip_depth and tag in BLOCK_TAGS:
            self._flush()
        if self.skip_depth and (tag in SKIP_TAGS or tag == "div"):
            self.skip_depth -= 1
        if self.stack:
            self.stack.pop()

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        text = html.unescape(data).replace("\xa0", " ")
        if text.strip():
            self.current.append(text)

    def close(self) -> None:
        super().close()
        self._flush()

    def _flush(self) -> None:
        if not self.current:
            return
        text = re.sub(r"\s+", " ", "".join(self.current)).strip()
        self.current.clear()
        if text and text not in {"Source:", "Downloaded:"}:
            self.chunks.append(text)


def load_candidates() -> list[dict[str, str]]:
    with CANDIDATE_PATH.open(encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def classify_candidate(row: dict[str, str]) -> dict[str, object]:
    en = row["english"]
    pos = row["pos"]
    suggested = row["suggested_class"]

    if en in EXACT_DECISIONS:
        cls, note = EXACT_DECISIONS[en]
        return decision(row, cls, zh=en, rationale=note, confidence="high")
    if en in BILINGUAL_TRANSLATIONS:
        return decision(row, "bilingual-first-use", zh=BILINGUAL_TRANSLATIONS[en], confidence="high")
    if en in COMMON_TRANSLATIONS:
        return decision(row, "translate", zh=COMMON_TRANSLATIONS[en], confidence="high")
    if en in TITLE_TRANSLATIONS:
        return decision(row, "context-title", zh=TITLE_TRANSLATIONS[en], confidence="medium")

    if pos in CONTEXT_TITLE_POS or suggested == "context-title":
        return decision(row, "context-title", zh=en, confidence="medium")
    if pos in CONTEXT_UI_POS or suggested == "context-ui-label":
        return decision(row, "context-ui-label", zh=en, confidence="medium")
    if pos in {"blend-mode", "filter-enum", "color-name", "step-mode"}:
        return decision(row, "context-ui-label", zh=en, confidence="medium")
    if pos in {"source-variant", "studio", "url", "filename", "config-file"}:
        return decision(row, "preserve", zh=en, confidence="high")
    if suggested == "translate-or-bilingual":
        return decision(row, "translate", zh="", rationale="needs Chinese prose rendering", confidence="low")
    return decision(row, "review-required", zh=row["current_chinese"], confidence="low")


def decision(
    row: dict[str, str],
    cls: str,
    zh: str,
    rationale: str = "",
    confidence: str = "medium",
) -> dict[str, object]:
    return {
        "en": row["english"],
        "current_zh": row["current_chinese"],
        "pos": row["pos"],
        "decision_class": cls,
        "recommended_zh": zh,
        "preserve_exact": cls in {"preserve", "context-ui-label", "context-title"},
        "flag_english_in_prose": cls in {"translate", "bilingual-first-use"},
        "confidence": confidence,
        "rationale": rationale or default_rationale(cls),
        "risk_reason": row["risk_reason"],
        "source_basis": [
            "RenderMan 27 local source HTML",
            "Pixar RenderMan official docs",
            "upstream standards where applicable",
        ],
    }


def default_rationale(cls: str) -> str:
    return {
        "translate": "ordinary technical prose should read naturally in Chinese",
        "bilingual-first-use": "technical acronym/term benefits from Chinese plus original form",
        "context-ui-label": "keep exact English when naming a UI/parameter label; translate surrounding prose",
        "context-title": "keep exact English for title/credit contexts; translate descriptive prose where needed",
        "preserve": "identifier, product name, file name, syntax, or proper noun",
        "review-required": "needs page-level context before final decision",
    }[cls]


def build_overrides() -> dict[str, object]:
    rows = load_candidates()
    decisions = [classify_candidate(row) for row in rows]
    summary = Counter(d["decision_class"] for d in decisions)
    high_conf = sum(1 for d in decisions if d["confidence"] in {"high", "medium"} and d["decision_class"] != "review-required")
    payload = {
        "metadata": {
            "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            "candidate_source": str(CANDIDATE_PATH.relative_to(ROOT)),
            "glossary_source": str(GLOSSARY_PATH.relative_to(ROOT)),
            "purpose": "Non-destructive decision overlay for terminology review.",
        },
        "summary": {
            "total_candidates": len(decisions),
            "decided_non_review_required": high_conf,
            "decision_class_counts": dict(sorted(summary.items())),
        },
        "decision_classes": {
            "preserve": "Exact protected product/API/file/syntax/proper-name form.",
            "translate": "Should be Chinese in prose.",
            "bilingual-first-use": "Use Chinese plus acronym/original on first use when helpful.",
            "context-ui-label": "Preserve exact label only when naming UI/parameter labels.",
            "context-title": "Preserve exact title/credit contexts; translate surrounding prose.",
            "review-required": "Needs manual page-context review before correction.",
        },
        "decisions": decisions,
    }
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    (AUDIT_DIR / "term-decision-overrides.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_decision_summary(payload)
    return payload


def write_decision_summary(payload: dict[str, object]) -> None:
    summary = payload["summary"]
    decisions = payload["decisions"]
    counts = summary["decision_class_counts"]
    lines = [
        "# Term Decision Overlay Summary",
        "",
        f"Generated: {payload['metadata']['generated_at']}",
        "",
        "## Counts",
        "",
        f"- Total candidates: {summary['total_candidates']}",
        f"- Decided non-review-required: {summary['decided_non_review_required']}",
    ]
    for key, value in counts.items():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Review-Required Sample", ""])
    for d in [d for d in decisions if d["decision_class"] == "review-required"][:40]:
        lines.append(f"- `{d['en']}` ({d['pos']}): {d['rationale']}")
    lines.extend(["", "## Translate/Bilingual Sample", ""])
    for d in [d for d in decisions if d["decision_class"] in {"translate", "bilingual-first-use"}][:60]:
        zh = d["recommended_zh"] or "TBD"
        lines.append(f"- `{d['en']}` -> {zh} [{d['decision_class']}]")
    (AUDIT_DIR / "term-decision-summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def load_decision_payload() -> dict[str, object]:
    path = AUDIT_DIR / "term-decision-overrides.json"
    if not path.exists():
        return build_overrides()
    return json.loads(path.read_text(encoding="utf-8"))


def extract_chunks(path: Path) -> list[str]:
    parser = VisibleTextExtractor()
    parser.feed(path.read_text(encoding="utf-8", errors="ignore"))
    parser.close()
    return parser.chunks


def compile_allowed_terms(decisions: list[dict[str, object]]) -> list[str]:
    terms = []
    for d in decisions:
        if d["decision_class"] in {"preserve", "context-ui-label", "context-title"}:
            en = str(d["en"])
            if len(en) >= 3:
                terms.append(en)
    return sorted(set(terms), key=len, reverse=True)


def strip_allowed(text: str, allowed_terms: list[str]) -> str:
    out = text
    for pat in PRIORITY_PROTECTED_PATTERNS:
        out = re.sub(pat, " ", out)
    for pat in sorted(PROTECTED_PATTERNS, key=len, reverse=True):
        out = re.sub(pat, " ", out)
    for term in allowed_terms:
        out = out.replace(term, " ")
    out = re.sub(r"\b[A-Za-z0-9_.+-]+/[A-Za-z0-9_./+-]+\b", " ", out)
    return out


def scan_pages() -> dict[str, object]:
    payload = load_decision_payload()
    decisions = payload["decisions"]
    allowed = compile_allowed_terms(decisions)
    flag_terms = [
        d for d in decisions if d["decision_class"] in {"translate", "bilingual-first-use"} and len(str(d["en"])) > 2
    ]
    pages = []
    for path in sorted(HTML_ZH_ROOT.rglob("*.html")):
        if path.name == "index.html":
            continue
        rel = str(path.relative_to(HTML_ZH_ROOT))
        chunks = extract_chunks(path)
        risky_chunks = []
        flagged_terms = Counter()
        residual_words = Counter()
        for chunk in chunks:
            has_zh = bool(re.search(r"[\u4e00-\u9fff]", chunk))
            if not has_zh:
                continue
            stripped = strip_allowed(chunk, allowed)
            chunk_flagged = []
            for d in flag_terms:
                en = str(d["en"])
                if re.search(rf"(?<![A-Za-z0-9_]){re.escape(en)}(?![A-Za-z0-9_])", stripped, re.IGNORECASE):
                    flagged_terms[en] += 1
                    chunk_flagged.append(en)
            words = [
                w
                for w in re.findall(r"\b[A-Za-z][A-Za-z'-]{2,}\b", stripped)
                if w.lower() not in {"source", "downloaded", "html", "http", "https"}
            ]
            for word in words:
                residual_words[word] += 1
            if len(words) >= 5 or chunk_flagged:
                risky_chunks.append(
                    {
                        "text": chunk[:260],
                        "flagged_terms": chunk_flagged[:20],
                        "residual_words": words[:30],
                    }
                )
        score = sum(flagged_terms.values()) * 10 + sum(residual_words.values())
        tier = "low"
        if score >= 200 and risky_chunks:
            tier = "high"
        elif score >= 50:
            tier = "medium"
        pages.append(
            {
                "path": rel,
                "risk_score": score,
                "risk_tier": tier,
                "flagged_terms": dict(flagged_terms.most_common(20)),
                "residual_english_words": dict(residual_words.most_common(30)),
                "sample_chunks": risky_chunks[:5],
            }
        )
    pages.sort(key=lambda x: (x["risk_score"], x["path"]), reverse=True)
    summary = Counter(p["risk_tier"] for p in pages)
    residual_terms = Counter()
    for page in pages:
        residual_terms.update(page["residual_english_words"])
    report = {
        "metadata": {
            "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            "html_root": str(HTML_ZH_ROOT.relative_to(ROOT)),
            "term_overlay": str((AUDIT_DIR / "term-decision-overrides.json").relative_to(ROOT)),
        },
        "summary": {
            "total_pages": len(pages),
            "risk_tier_counts": dict(sorted(summary.items())),
            "flagged_term_count": sum(len(p["flagged_terms"]) for p in pages),
            "residual_term_candidate_count": len(residual_terms),
        },
        "residual_term_candidates": [
            {
                "term": term,
                "count": count,
                "suggested_zh": RESIDUAL_WORD_TRANSLATIONS.get(term.lower(), ""),
                "status": "needs-termbase-decision",
            }
            for term, count in residual_terms.most_common(300)
        ],
        "pages": pages,
    }
    (AUDIT_DIR / "page-risk-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_residual_candidates_tsv(report)
    write_page_report_md(report)
    return report


def write_residual_candidates_tsv(report: dict[str, object]) -> None:
    path = AUDIT_DIR / "residual-term-candidates.tsv"
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["term", "count", "suggested_zh", "status"],
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(report["residual_term_candidates"])


def write_page_report_md(report: dict[str, object]) -> None:
    lines = [
        "# Page Terminology Risk Report",
        "",
        f"Generated: {report['metadata']['generated_at']}",
        "",
        "## Summary",
        "",
        f"- Total pages: {report['summary']['total_pages']}",
    ]
    for key, value in report["summary"]["risk_tier_counts"].items():
        lines.append(f"- {key}: {value}")
    lines.append(f"- Residual term candidates: {report['summary']['residual_term_candidate_count']}")
    lines.extend(["", "## Top Residual Term Candidates", ""])
    for item in report["residual_term_candidates"][:80]:
        zh = item["suggested_zh"] or "TBD"
        lines.append(f"- `{item['term']}` x{item['count']} -> {zh}")
    lines.extend(["", "## Highest-Risk Pages", ""])
    for page in report["pages"][:40]:
        lines.append(f"### {page['path']}")
        lines.append("")
        lines.append(f"- Tier: {page['risk_tier']}")
        lines.append(f"- Score: {page['risk_score']}")
        if page["flagged_terms"]:
            terms = ", ".join(f"`{k}` x{v}" for k, v in page["flagged_terms"].items())
            lines.append(f"- Flagged terms: {terms}")
        if page["residual_english_words"]:
            words = ", ".join(f"`{k}` x{v}" for k, v in list(page["residual_english_words"].items())[:12])
            lines.append(f"- Residual words: {words}")
        for chunk in page["sample_chunks"][:2]:
            lines.append(f"- Sample: {chunk['text']}")
        lines.append("")
    while lines and not lines[-1]:
        lines.pop()
    (AUDIT_DIR / "page-risk-report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "command",
        choices=["build-overrides", "scan-pages", "all"],
        nargs="?",
        default="all",
    )
    args = parser.parse_args()
    if args.command in {"build-overrides", "all"}:
        payload = build_overrides()
        print(json.dumps(payload["summary"], ensure_ascii=False, indent=2))
    if args.command in {"scan-pages", "all"}:
        report = scan_pages()
        print(json.dumps(report["summary"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
