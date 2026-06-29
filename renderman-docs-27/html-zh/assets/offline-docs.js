(function () {
  function rootPrefix() {
    var path = decodeURIComponent(window.location.pathname);
    var marker = "/html-zh/";
    var index = path.lastIndexOf(marker);
    if (index === -1) return "";
    var rel = path.slice(index + marker.length);
    var depth = rel.split("/").length - 1;
    return depth > 0 ? "../".repeat(depth) : "";
  }

  function currentRel() {
    var path = decodeURIComponent(window.location.pathname);
    var marker = "/html-zh/";
    var index = path.lastIndexOf(marker);
    return index === -1 ? "index.html" : path.slice(index + marker.length);
  }

  function currentSpace(rel) {
    if (rel.indexOf("/") === -1) return "";
    return rel.split("/")[0];
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, function (char) {
      return {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;"
      }[char];
    });
  }

  function queryTerms(query) {
    var q = query.toLowerCase();
    var terms = [q];
    var hints = [
      ["许可", ["license", "licensing"]],
      ["许可证", ["license", "licensing"]],
      ["安装", ["install", "installation"]],
      ["材质", ["material", "materials"]],
      ["着色", ["shading", "shader"]],
      ["灯光", ["light", "lighting"]],
      ["体积", ["volume", "volumes"]],
      ["几何", ["geometry"]],
      ["渲染", ["render", "rendering"]],
      ["纹理", ["texture", "texturing"]],
      ["相机", ["camera", "cameras"]]
    ];
    hints.forEach(function (hint) {
      if (q.indexOf(hint[0]) !== -1) {
        hint[1].forEach(function (term) {
          if (terms.indexOf(term) === -1) terms.push(term);
        });
      }
    });
    return terms;
  }

  function navItems(prefix) {
    return [
      ["RenderMan", "REN27/542212097-RenderMan 27 Documentation.html", "REN27"],
      ["Maya", "RFM27/544538625-RenderMan 27 for Maya.html", "RFM27"],
      ["Katana", "RFK27/546177025-RenderMan 27 for Katana.html", "RFK27"],
      ["Houdini", "RFH27/544640331-RenderMan 27 for Houdini.html", "RFH27"],
      ["Blender", "RFB27/544636929-RenderMan 27 for Blender.html", "RFB27"],
      ["Tractor", "TRA/22183944-Tractor 2.html", "TRA"],
      ["FAQs", "https://renderman.pixar.com/general-faq", "FAQ"],
      ["RenderMan University", "RU/476283147-RenderMan University Home.html", "RU"]
    ].map(function (item) {
      var href = /^https?:/.test(item[1]) ? item[1] : prefix + item[1];
      return { label: item[0], href: href, space: item[2] };
    });
  }

  function sectionMeta(space) {
    var data = {
      REN27: {
        title: "RenderMan 27",
        desc: "核心渲染器文档，包括安装、几何、材质、灯光、渲染设置、XPU、RIS、工具和发行说明。",
        home: "REN27/542212097-RenderMan 27 Documentation.html"
      },
      RFM27: {
        title: "RenderMan for Maya",
        desc: "面向 Maya 的 RenderMan 工作流，包括安装、场景设置、材质、灯光、AOV、渲染和开发者指南。",
        home: "RFM27/544538625-RenderMan 27 for Maya.html"
      },
      RFK27: {
        title: "RenderMan for Katana",
        desc: "面向 Katana 的 RenderMan 工作流，包括环境配置、场景设置、几何、材质、灯光和渲染。",
        home: "RFK27/546177025-RenderMan 27 for Katana.html"
      },
      RFH27: {
        title: "RenderMan for Houdini",
        desc: "面向 Houdini 与 Solaris 的 RenderMan 工作流，包括 LOP、材质、灯光、AOV、渲染和 Tractor。",
        home: "RFH27/544640331-RenderMan 27 for Houdini.html"
      },
      RFB27: {
        title: "RenderMan for Blender",
        desc: "面向 Blender 的 RenderMan 文档，包括安装、材质、灯光、渲染、AOV、示例和高级配置。",
        home: "RFB27/544636929-RenderMan 27 for Blender.html"
      },
      TRA: {
        title: "Tractor",
        desc: "Tractor 分布式队列系统文档，包括 engine、blade、spool、Dashboard、API、配置和升级。",
        home: "TRA/22183944-Tractor 2.html"
      },
      RU: {
        title: "RenderMan University",
        desc: "RenderMan University 教程与项目资源，包括基础课程、示例场景、项目路径和学习材料。",
        home: "RU/476283147-RenderMan University Home.html"
      }
    };
    return data[space] || null;
  }

  function sectionPages(space) {
    var pages = (window.RM_DOCS_PAGES || []).filter(function (page) {
      return page.space === space;
    });
    var preferred = /(home|documentation|getting started|installation|licensing|scene setup|geometry|materials?|shading|lighting|rendering|examples|release notes|dashboard|configuration)/i;
    var scored = pages.map(function (page) {
      var score = preferred.test(page.title) ? 0 : 1;
      if (/home|documentation/i.test(page.title)) score = -1;
      return { page: page, score: score };
    });
    scored.sort(function (a, b) {
      if (a.score !== b.score) return a.score - b.score;
      return a.page.title.localeCompare(b.page.title, "zh-Hans-u-co-pinyin");
    });
    return scored.slice(0, 8).map(function (item) { return item.page; });
  }

  function injectSectionPanel(prefix, rel) {
    var main = document.querySelector("main");
    if (!main || rel === "index.html" || rel === "") return;
    var space = currentSpace(rel);
    var meta = sectionMeta(space);
    if (!meta) return;
    var isLanding = rel === meta.home || / Home\.html$/.test(rel);
    if (isLanding) {
      var panel = document.createElement("section");
      panel.className = "rm-doc-section-panel";
      var cards = sectionPages(space).map(function (page) {
        return '<a class="rm-section-card" href="' + escapeHtml(prefix + page.path) + '"><strong>' + escapeHtml(page.title) + '</strong><span>' + escapeHtml(page.space) + '</span></a>';
      }).join("");
      panel.innerHTML =
        '<div class="rm-section-panel-inner">' +
        '<p class="rm-section-eyebrow">RenderMan Docs</p>' +
        '<h1>' + escapeHtml(meta.title) + '</h1>' +
        '<p>' + escapeHtml(meta.desc) + '</p>' +
        '<div class="rm-section-cards">' + cards + '</div>' +
        '</div>';
      main.parentNode.insertBefore(panel, main);
      return;
    }
    var strip = document.createElement("div");
    strip.className = "rm-doc-breadcrumb-strip";
    strip.innerHTML =
      '<div class="rm-doc-breadcrumb-inner">' +
      '<a href="' + escapeHtml(prefix + 'index.html') + '">RenderMan 27 Docs</a>' +
      '<span>/</span>' +
      '<a href="' + escapeHtml(prefix + meta.home) + '">' + escapeHtml(meta.title) + '</a>' +
      '</div>';
    main.parentNode.insertBefore(strip, main);
  }

  function buildHeader(prefix, rel) {
    var active = currentSpace(rel);
    var header = document.createElement("div");
    header.innerHTML =
      '<header class="rm-site-header">' +
      '  <div class="rm-header-inner">' +
      '    <a class="rm-logo" href="' + prefix + 'index.html" aria-label="RenderMan 27 Docs">' +
      '      <svg class="rm-logo-mark" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 32 32" aria-hidden="true"><path fill="currentColor" fill-rule="evenodd" d="M32 0H0v32h32V0ZM2.284 2.286v27.428h9.812v-7.993h1.598l4.974 7.993h11.045l-6.39-9.717c3.286-1.529 5.477-4.076 5.477-8.033v-.235c0-2.86-1.004-4.937-2.875-6.544-2.145-1.842-5.568-2.9-10.497-2.9H2.284ZM15.291 15.49h-3.195V9.417h3.24c2.146 0 3.56.98 3.56 2.939v.196c0 1.92-1.414 2.938-3.605 2.938Z" clip-rule="evenodd"/></svg>' +
      '      <span class="rm-logo-word">RENDERMAN <strong>27</strong> <span>DOCS</span></span>' +
      '      <span class="rm-logo-caret" aria-hidden="true"></span>' +
      '    </a>' +
      '    <a class="rm-main-site" href="https://renderman.pixar.com/" target="_blank" rel="noreferrer">主站</a>' +
      '  </div>' +
      '</header>' +
      '<nav class="rm-product-nav" aria-label="产品导航">' +
      '  <div class="rm-nav-inner"></div>' +
      '</nav>';
    var nav = header.querySelector(".rm-nav-inner");
    navItems(prefix).forEach(function (item) {
      var a = document.createElement("a");
      a.className = "rm-nav-link";
      a.href = item.href;
      a.textContent = item.label;
      if (active && item.space === active) a.setAttribute("aria-current", "page");
      nav.appendChild(a);
    });
    var button = document.createElement("button");
    button.className = "rm-nav-search";
    button.type = "button";
    button.setAttribute("aria-label", "搜索");
    nav.appendChild(button);
    return header;
  }

  function searchHref(prefix, page) {
    return prefix + page.path;
  }

  function renderResults(container, query, prefix) {
    var pages = window.RM_DOCS_PAGES || [];
    var q = query.trim().toLowerCase();
    var terms = queryTerms(q);
    container.innerHTML = "";
    if (!q) {
      pages.slice(0, 12).forEach(function (page) {
        addResult(container, page, prefix);
      });
      return;
    }
    var matches = [];
    pages.forEach(function (page) {
      var haystack = (page.title + " " + page.space + " " + page.path + " " + (page.search || "")).toLowerCase();
      var matchedTerm = "";
      var firstIndex = -1;
      terms.some(function (term) {
        var index = haystack.indexOf(term);
        if (index !== -1) {
          matchedTerm = term;
          firstIndex = index;
          return true;
        }
        return false;
      });
      if (matchedTerm) {
        var title = page.title.toLowerCase();
        var path = page.path.toLowerCase();
        var score = 10000 + firstIndex;
        terms.forEach(function (term) {
          if (title.indexOf(term) !== -1) score = Math.min(score, 0 + title.indexOf(term));
          if (path.indexOf(term) !== -1) score = Math.min(score, 100 + path.indexOf(term));
        });
        if ((page.excerpt || "").toLowerCase().indexOf(q) !== -1) score = Math.min(score, 500);
        matches.push({ page: page, score: score });
      }
    });
    matches.sort(function (a, b) {
      if (a.score !== b.score) return a.score - b.score;
      return a.page.title.localeCompare(b.page.title, "zh-Hans-u-co-pinyin");
    });
    matches.slice(0, 40).forEach(function (item) {
      addResult(container, item.page, prefix, q);
    });
    if (!matches.length) {
      var empty = document.createElement("div");
      empty.className = "rm-empty-search";
      empty.textContent = "没有匹配的页面";
      container.appendChild(empty);
    }
  }

  function addResult(container, page, prefix, query) {
    var a = document.createElement("a");
    a.href = searchHref(prefix, page);
    var detail = page.space + " / " + page.path;
    if (query && page.excerpt) detail += " · " + page.excerpt;
    a.innerHTML = escapeHtml(page.title) + "<span>" + escapeHtml(detail) + "</span>";
    container.appendChild(a);
  }

  function pagesForSpace(space) {
    return (window.RM_DOCS_PAGES || []).filter(function (page) {
      return page.space === space;
    });
  }

  function buildSpaceNavigation(prefix, rel) {
    var space = currentSpace(rel);
    var meta = sectionMeta(space);
    var pages = pagesForSpace(space);
    if (!space || !meta || !pages.length) return null;
    var aside = document.createElement("aside");
    aside.className = "rm-space-navigation";
    var items = pages.map(function (page) {
      var current = page.path === rel;
      return '<li><a class="rm-page-node" href="' + escapeHtml(prefix + page.path) + '"' +
        (current ? ' aria-current="page"' : '') +
        ' data-title="' + escapeHtml(page.title.toLowerCase()) + '">' +
        escapeHtml(page.title) +
        '</a></li>';
    }).join("");
    aside.innerHTML =
      '<div class="rm-space-navigation-inner">' +
      '<p class="rm-sidebar-kicker">章节导航</p>' +
      '<h2 class="rm-sidebar-title">' + escapeHtml(meta.title) + '</h2>' +
      '<label class="rm-sidebar-search"><input type="search" placeholder="筛选页面" autocomplete="off"></label>' +
      '<ul class="rm-page-tree">' + items + '</ul>' +
      '</div>';
    var filter = aside.querySelector("input");
    filter.addEventListener("input", function () {
      var q = filter.value.trim().toLowerCase();
      aside.querySelectorAll(".rm-page-node").forEach(function (node) {
        node.classList.toggle("is-hidden", q && node.dataset.title.indexOf(q) === -1);
      });
    });
    return aside;
  }

  function sizeSpaceNavigationScroller(scroller) {
    if (!scroller) return;
    var rect = scroller.getBoundingClientRect();
    var available = Math.max(360, window.innerHeight - rect.top - 24);
    scroller.style.maxHeight = Math.round(available) + "px";
  }

  function enhanceDocLayout(prefix, rel) {
    if (rel === "index.html" || rel === "") return;
    var main = document.querySelector("main");
    if (!main || main.closest(".rm-doc-layout")) return;
    var aside = buildSpaceNavigation(prefix, rel);
    if (!aside) return;
    var layout = document.createElement("div");
    layout.className = "rm-doc-layout";
    main.parentNode.insertBefore(layout, main);
    layout.appendChild(aside);
    layout.appendChild(main);
    document.body.classList.add("rm-has-space-navigation");
    var current = aside.querySelector('.rm-page-node[aria-current="page"]');
    var scroller = aside.querySelector(".rm-space-navigation-inner");
    if (current && scroller) {
      window.requestAnimationFrame(function () {
        sizeSpaceNavigationScroller(scroller);
        var scrollerRect = scroller.getBoundingClientRect();
        var currentRect = current.getBoundingClientRect();
        var delta = currentRect.top - scrollerRect.top;
        scroller.scrollTop = Math.max(0, scroller.scrollTop + delta - Math.round(scroller.clientHeight * 0.35));
      });
      window.addEventListener("resize", function () {
        sizeSpaceNavigationScroller(scroller);
      });
    }
  }

  function buildSearchPanel(prefix) {
    var panel = document.createElement("div");
    panel.className = "rm-search-panel";
    panel.innerHTML =
      '<div class="rm-search-box" role="dialog" aria-modal="true" aria-label="搜索文档">' +
      '  <div class="rm-search-head"><strong>搜索 RenderMan 27 文档</strong><button class="rm-search-close" type="button" aria-label="关闭">×</button></div>' +
      '  <label class="rm-search-field"><input type="search" placeholder="搜索..." autocomplete="off"></label>' +
      '  <div class="rm-search-results"></div>' +
      '</div>';
    var input = panel.querySelector("input");
    var results = panel.querySelector(".rm-search-results");
    input.addEventListener("input", function () {
      renderResults(results, input.value, prefix);
    });
    panel.querySelector(".rm-search-close").addEventListener("click", function () {
      document.body.classList.remove("rm-search-open");
    });
    panel.addEventListener("click", function (event) {
      if (event.target === panel) document.body.classList.remove("rm-search-open");
    });
    renderResults(results, "", prefix);
    return panel;
  }

  function wireHomeSearch(prefix) {
    var input = document.querySelector("[data-rm-home-search]");
    if (!input) return;
    input.addEventListener("focus", function () {
      document.body.classList.add("rm-search-open");
      var panelInput = document.querySelector(".rm-search-panel input");
      if (panelInput) {
        panelInput.value = input.value;
        panelInput.dispatchEvent(new Event("input"));
        setTimeout(function () { panelInput.focus(); }, 0);
      }
    });
  }

  function init() {
    if (document.querySelector(".rm-site-header")) return;
    var prefix = rootPrefix();
    var rel = currentRel();
    var isHome = rel === "index.html" || rel === "";
    document.body.classList.add("rm-themed");
    document.body.classList.add(isHome ? "rm-home" : "rm-doc-page");

    var first = document.body.firstChild;
    document.body.insertBefore(buildHeader(prefix, rel), first);
    injectSectionPanel(prefix, rel);
    enhanceDocLayout(prefix, rel);
    document.body.appendChild(buildSearchPanel(prefix));

    var searchButton = document.querySelector(".rm-nav-search");
    searchButton.addEventListener("click", function () {
      document.body.classList.add("rm-search-open");
      var input = document.querySelector(".rm-search-panel input");
      if (input) setTimeout(function () { input.focus(); }, 0);
    });

    wireHomeSearch(prefix);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
