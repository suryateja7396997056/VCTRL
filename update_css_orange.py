import re

css = """
    :root {
      --bg-main: #ffffff;
      --bg-sec: #fafafa;
      --bg-dark: #0a0a0a;
      --charcoal: #111827;
      --text-main: #1f2937;
      --text-muted: #6b7280;
      --orange: #FF5722;
      --orange-light: #FFF0EB;
      --orange-dark: #E64A19;
      --white: #ffffff;
      --line: rgba(0, 0, 0, 0.08);
      --line-dark: rgba(255, 255, 255, 0.1);
      --glass: rgba(255, 255, 255, 0.85);
      --glass-dark: rgba(10, 10, 10, 0.85);
      --shadow: 0 24px 50px rgba(0, 0, 0, 0.04);
      --shadow-lg: 0 40px 80px rgba(0, 0, 0, 0.08);
      --shadow-orange: 0 20px 40px rgba(255, 87, 34, 0.2);
      --radius: 16px;
      --radius-sm: 8px;
      --container: 1280px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
      overflow-x: hidden;
      background: var(--bg-main);
    }

    body {
      min-width: 320px;
      overflow-x: hidden;
      background: var(--bg-main);
      color: var(--text-main);
      font-family: "Plus Jakarta Sans", sans-serif;
      line-height: 1.8;
      text-rendering: optimizeLegibility;
      -webkit-font-smoothing: antialiased;
    }

    img {
      display: block;
      max-width: 100%;
    }

    a {
      color: inherit;
      text-decoration: none;
    }

    button {
      border: 0;
      font: inherit;
    }

    .container {
      width: min(100% - 40px, var(--container));
      margin-inline: auto;
    }

    .eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 16px;
      color: var(--orange);
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 0.2em;
      text-transform: uppercase;
    }

    .eyebrow::before {
      content: "";
      width: 40px;
      height: 2px;
      background: var(--orange);
    }

    .section-title {
      color: var(--charcoal);
      font-size: clamp(2.5rem, 4vw, 4rem);
      line-height: 1.15;
      letter-spacing: -0.03em;
      font-weight: 800;
    }

    .dark-section .section-title {
      color: var(--white);
    }

    .section-subtitle {
      max-width: 720px;
      margin-top: 24px;
      color: var(--text-muted);
      font-size: 1.15rem;
      font-weight: 400;
      line-height: 1.8;
    }

    .gradient-text {
      background: linear-gradient(135deg, var(--orange) 0%, var(--orange-dark) 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
    }

    .btn {
      position: relative;
      isolation: isolate;
      display: inline-flex;
      min-height: 56px;
      align-items: center;
      justify-content: center;
      gap: 12px;
      padding: 16px 36px;
      border-radius: 50px;
      cursor: pointer;
      font-size: 0.95rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      white-space: nowrap;
      overflow: hidden;
    }

    .btn::before {
      content: "";
      position: absolute;
      inset: 0;
      z-index: -1;
      background: rgba(0, 0, 0, 0.1);
      transform: scaleX(0);
      transform-origin: right;
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .btn:hover::before {
      transform: scaleX(1);
      transform-origin: left;
    }

    .btn:hover {
      transform: translateY(-3px);
    }

    .btn-primary {
      background: var(--orange);
      color: var(--white);
      border: 1px solid transparent;
      box-shadow: var(--shadow-orange);
    }

    .btn-primary:hover {
      box-shadow: 0 24px 48px rgba(255, 87, 34, 0.3);
      color: var(--white);
    }

    .btn-secondary {
      border: 2px solid var(--line);
      background: var(--white);
      color: var(--charcoal);
    }

    .btn-secondary:hover {
      border-color: var(--orange);
      color: var(--orange);
      background: var(--orange-light);
    }

    .btn-light {
      border: 1px solid transparent;
      background: var(--bg-sec);
      color: var(--charcoal);
    }

    .btn-light:hover {
      background: var(--orange-light);
      color: var(--orange);
    }

    .icon-button {
      display: inline-grid;
      width: 44px;
      height: 44px;
      place-items: center;
      border: 1px solid var(--line);
      border-radius: 50%;
      background: var(--white);
      color: var(--text-muted);
      transition: all 0.4s ease;
    }

    .icon-button:hover {
      border-color: var(--orange);
      background: var(--orange);
      color: var(--white);
      transform: translateY(-2px);
      box-shadow: var(--shadow-orange);
    }

    .dark-section .icon-button {
      background: rgba(255, 255, 255, 0.05);
      border-color: var(--line-dark);
    }

    /* Header */
    .site-header {
      position: fixed;
      inset: 0 0 auto;
      z-index: 50;
      border-bottom: 1px solid transparent;
      background: transparent;
      transition: all 0.5s ease;
    }

    .site-header.scrolled {
      border-color: var(--line);
      background: var(--glass);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      box-shadow: var(--shadow);
    }

    .nav {
      display: flex;
      height: 100px;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
      transition: height 0.4s ease;
    }

    .site-header.scrolled .nav {
      height: 76px;
    }

    .brand {
      display: inline-flex;
      min-width: max-content;
      align-items: center;
      gap: 12px;
      color: var(--charcoal);
      font-weight: 800;
      letter-spacing: 0;
    }

    .brand-logo-plate {
      display: inline-flex;
      width: auto;
      height: 50px;
      align-items: center;
      justify-content: center;
    }

    .brand-logo {
      height: 100%;
      width: auto;
      object-fit: contain;
    }

    .brand-text {
      display: none;
    }

    .nav-menu {
      display: flex;
      align-items: center;
      gap: 36px;
      color: var(--text-main);
      font-size: 0.95rem;
      font-weight: 600;
    }

    .nav-link {
      position: relative;
      padding-block: 8px;
      transition: color 0.3s ease;
    }

    .nav-link::after {
      content: "";
      position: absolute;
      right: 0;
      bottom: 0;
      left: 0;
      height: 2px;
      background: var(--orange);
      transform: scaleX(0);
      transform-origin: right;
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .nav-link:hover {
      color: var(--orange);
    }

    .nav-link:hover::after {
      transform: scaleX(1);
      transform-origin: left;
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 20px;
    }

    .socials {
      display: flex;
      gap: 12px;
    }

    .menu-toggle {
      display: none;
      width: 48px;
      height: 48px;
      place-items: center;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--white);
      color: var(--charcoal);
      cursor: pointer;
    }

    /* Hero */
    .hero {
      position: relative;
      min-height: 100svh;
      display: grid;
      align-items: center;
      overflow: hidden;
      padding: 160px 0 80px;
      background: var(--bg-sec);
    }

    .hero::before {
      content: "";
      position: absolute;
      inset: 0;
      opacity: 0.4;
      background-image:
        linear-gradient(var(--line) 1px, transparent 1px),
        linear-gradient(90deg, var(--line) 1px, transparent 1px);
      background-size: 80px 80px;
      mask-image: linear-gradient(180deg, #000 0%, transparent 100%);
    }

    .hero::after {
      content: "";
      position: absolute;
      width: 60vw;
      height: 60vw;
      right: -10vw;
      top: -10vw;
      border-radius: 50%;
      background: radial-gradient(circle, var(--orange-light), transparent 70%);
      opacity: 0.5;
      z-index: 0;
      animation: floatGlow 12s ease-in-out infinite;
    }

    .hero-inner {
      position: relative;
      z-index: 2;
      display: grid;
      grid-template-columns: minmax(0, 1.1fr) minmax(360px, 0.9fr);
      gap: clamp(40px, 6vw, 80px);
      align-items: center;
    }

    .hero-copy {
      max-width: 860px;
    }

    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 24px;
      padding: 12px 20px;
      border: 1px solid var(--orange);
      border-radius: 50px;
      background: var(--orange-light);
      color: var(--orange-dark);
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      opacity: 0;
      transform: translateY(20px);
      animation: heroIn 0.8s ease forwards 0.15s;
    }

    .hero-badge i {
      color: var(--orange);
    }

    .hero h1 {
      max-width: 900px;
      color: var(--charcoal);
      font-size: clamp(3.5rem, 5vw, 5.5rem);
      line-height: 1.05;
      font-weight: 800;
      letter-spacing: -0.03em;
      opacity: 0;
      transform: translateY(30px);
      animation: heroIn 1s cubic-bezier(0.16, 1, 0.3, 1) forwards 0.3s;
    }

    .hero p {
      max-width: 680px;
      margin-top: 24px;
      color: var(--text-muted);
      font-size: clamp(1.1rem, 1.5vw, 1.25rem);
      line-height: 1.8;
      font-weight: 400;
      opacity: 0;
      transform: translateY(22px);
      animation: heroIn 1s ease forwards 0.45s;
    }

    .hero-ctas {
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
      margin-top: 40px;
      opacity: 0;
      transform: translateY(20px);
      animation: heroIn 1s ease forwards 0.6s;
    }

    .hero-metrics {
      display: grid;
      grid-template-columns: repeat(4, minmax(120px, 1fr));
      gap: 16px;
      max-width: 800px;
      margin-top: 48px;
      opacity: 0;
      transform: translateY(18px);
      animation: heroIn 1s ease forwards 0.75s;
    }

    .hero-visual {
      position: relative;
      min-height: 600px;
      opacity: 0;
      transform: translateY(30px) scale(0.95);
      animation: heroIn 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards 0.86s;
    }

    .visual-card {
      position: absolute;
      overflow: hidden;
      border: 1px solid var(--line);
      border-radius: var(--radius);
      background: var(--white);
      box-shadow: var(--shadow-lg);
    }

    .main-visual {
      inset: 40px 0 40px 40px;
    }

    .main-visual img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    .visual-readout {
      position: absolute;
      z-index: 3;
      right: -20px;
      bottom: 60px;
      min-width: 220px;
      border: 1px solid var(--line);
      border-radius: var(--radius-sm);
      padding: 24px;
      background: var(--glass);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      box-shadow: var(--shadow);
    }

    .visual-readout span,
    .floating-panel span {
      display: block;
      color: var(--text-muted);
      font-size: 0.85rem;
      font-weight: 600;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }

    .visual-readout strong,
    .floating-panel strong {
      display: block;
      margin-top: 8px;
      color: var(--charcoal);
      font-size: 2.2rem;
      line-height: 1;
      font-weight: 800;
      letter-spacing: -0.02em;
    }

    .floating-panel {
      position: absolute;
      z-index: 4;
      display: grid;
      grid-template-columns: 56px auto;
      column-gap: 20px;
      align-items: center;
      min-width: 260px;
      border: 1px solid var(--line);
      border-radius: var(--radius-sm);
      padding: 24px;
      background: var(--glass);
      box-shadow: var(--shadow-lg);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      animation: floatPanel 6s ease-in-out infinite;
    }

    .floating-panel i {
      display: grid;
      width: 56px;
      height: 56px;
      grid-row: span 2;
      place-items: center;
      border-radius: 50%;
      background: var(--orange-light);
      color: var(--orange);
      font-size: 1.4rem;
    }

    .floating-panel strong {
      font-size: 1.6rem;
    }

    .panel-top {
      top: 20px;
      left: -20px;
    }

    .panel-bottom {
      display: none; /* Keep clean */
    }

    .metric {
      border: 1px solid var(--line);
      border-radius: var(--radius-sm);
      padding: 20px;
      background: var(--white);
      transition: all 0.3s ease;
    }
    .metric:hover {
      border-color: var(--orange);
      transform: translateY(-4px);
      box-shadow: var(--shadow);
    }

    .metric strong {
      display: block;
      color: var(--charcoal);
      font-size: clamp(1.5rem, 2vw, 2rem);
      line-height: 1.1;
      font-weight: 800;
    }

    .metric span {
      display: block;
      margin-top: 8px;
      color: var(--text-muted);
      font-size: 0.8rem;
      font-weight: 600;
      text-transform: uppercase;
    }

    .scroll-cue {
      position: absolute;
      z-index: 3;
      left: 50%;
      bottom: 40px;
      transform: translateX(-50%);
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 16px;
      color: var(--text-muted);
      font-size: 0.8rem;
      font-weight: 600;
      letter-spacing: 0.1em;
      text-transform: uppercase;
    }

    .scroll-cue span {
      width: 2px;
      height: 40px;
      background: linear-gradient(180deg, var(--orange), transparent);
      animation: scrollLine 2s ease-in-out infinite;
    }

    .capability-band {
      position: relative;
      z-index: 5;
      margin-top: -80px;
    }

    .capability-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      border-radius: var(--radius);
      overflow: hidden;
      background: var(--white);
      box-shadow: var(--shadow-lg);
    }

    .capability-item {
      min-height: 220px;
      padding: 48px 32px;
      border-right: 1px solid var(--line);
      transition: all 0.4s ease;
      background: var(--white);
    }

    .capability-item:hover {
      background: var(--orange-light);
    }

    .capability-item:last-child {
      border-right: 0;
    }

    .capability-item i {
      color: var(--orange);
      font-size: 2rem;
    }

    .capability-item h3 {
      margin-top: 24px;
      color: var(--charcoal);
      font-size: 1.4rem;
      font-weight: 800;
      line-height: 1.3;
    }

    .capability-item p {
      margin-top: 12px;
      color: var(--text-muted);
      font-size: 1rem;
      line-height: 1.6;
    }

    /* Sections */
    section {
      position: relative;
    }

    .section-pad {
      padding: 160px 0;
    }

    .about-grid {
      display: grid;
      grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr);
      gap: 80px;
      align-items: center;
    }

    .image-frame {
      position: relative;
      border-radius: var(--radius);
      overflow: hidden;
      box-shadow: var(--shadow-lg);
    }

    .image-frame::after {
      content: "";
      position: absolute;
      inset: 0;
      border: 1px solid rgba(0,0,0,0.05);
      border-radius: var(--radius);
      pointer-events: none;
    }

    .image-frame img {
      width: 100%;
      min-height: 600px;
      object-fit: cover;
    }

    .about-copy > p {
      margin-top: 24px;
      color: var(--text-muted);
      font-size: 1.1rem;
      line-height: 1.8;
    }

    .feature-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      margin: 40px 0;
    }

    .feature-card,
    .why-card,
    .product-card,
    .review-card,
    .client-card {
      border-radius: var(--radius-sm);
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .feature-card {
      border: 1px solid var(--line);
      padding: 32px 24px;
      background: var(--bg-main);
    }

    .feature-card i {
      display: grid;
      width: 56px;
      height: 56px;
      place-items: center;
      border-radius: 50%;
      background: var(--orange-light);
      color: var(--orange);
      font-size: 1.4rem;
    }

    .feature-card h3 {
      margin-top: 20px;
      color: var(--charcoal);
      font-size: 1.15rem;
      font-weight: 700;
      line-height: 1.4;
    }

    .feature-card:hover {
      transform: translateY(-8px);
      box-shadow: var(--shadow);
      border-color: var(--orange);
    }

    .products {
      background: var(--bg-sec);
      border-top: 1px solid var(--line);
      border-bottom: 1px solid var(--line);
    }

    .section-head {
      display: flex;
      align-items: end;
      justify-content: space-between;
      gap: 40px;
      margin-bottom: 60px;
    }

    .section-head .section-subtitle {
      margin-top: 0;
    }

    .product-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 40px;
    }

    .product-card {
      position: relative;
      overflow: hidden;
      border: 1px solid var(--line);
      background: var(--white);
      box-shadow: var(--shadow);
    }

    .product-media {
      position: relative;
      height: 280px;
      overflow: hidden;
      background: var(--bg-sec);
    }

    .product-media img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .product-body {
      padding: 40px 32px;
    }

    .product-body h3 {
      color: var(--charcoal);
      font-size: 1.6rem;
      line-height: 1.3;
      font-weight: 800;
    }

    .product-body p {
      margin-top: 16px;
      color: var(--text-muted);
      font-size: 1rem;
      line-height: 1.6;
    }

    .micro-cta {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      margin-top: 32px;
      color: var(--orange);
      font-size: 0.95rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      transition: gap 0.3s ease;
    }

    .product-card:hover {
      border-color: var(--orange);
      box-shadow: var(--shadow-lg);
      transform: translateY(-8px);
    }

    .product-card:hover img {
      transform: scale(1.08);
    }
    
    .product-card:hover .micro-cta {
      gap: 16px;
    }

    .dark-section {
      background: var(--bg-dark);
      color: var(--white);
    }

    .sector-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 20px;
      margin-top: 60px;
    }

    .sector-card {
      display: flex;
      min-height: 100px;
      align-items: center;
      gap: 16px;
      border: 1px solid var(--line-dark);
      border-radius: var(--radius-sm);
      padding: 24px;
      background: rgba(255, 255, 255, 0.03);
      color: var(--text-muted);
      font-size: 1.05rem;
      font-weight: 500;
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .sector-card i {
      flex: 0 0 auto;
      color: var(--orange);
      font-size: 1.4rem;
    }

    .sector-card:hover {
      border-color: var(--orange);
      background: rgba(255, 87, 34, 0.1);
      color: var(--white);
      transform: translateY(-6px);
    }

    .why-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 30px;
      margin-top: 60px;
    }

    .why-card {
      min-height: 320px;
      border: 1px solid var(--line);
      border-radius: var(--radius);
      padding: 48px 40px;
      background: var(--white);
      box-shadow: var(--shadow);
    }

    .why-card i {
      display: grid;
      width: 72px;
      height: 72px;
      place-items: center;
      border-radius: 50%;
      background: var(--orange-light);
      color: var(--orange);
      font-size: 1.8rem;
      transition: all 0.4s ease;
    }

    .why-card h3 {
      margin-top: 32px;
      color: var(--charcoal);
      font-size: 1.5rem;
      line-height: 1.3;
      font-weight: 800;
    }

    .why-card p {
      margin-top: 16px;
      color: var(--text-muted);
      font-size: 1.05rem;
      line-height: 1.6;
    }

    .why-card:hover {
      border-color: var(--orange);
      transform: translateY(-8px);
      box-shadow: var(--shadow-lg);
    }

    .impact {
      padding: 160px 0;
      background:
        linear-gradient(90deg, rgba(17, 24, 39, 0.95), rgba(17, 24, 39, 0.85)),
        url("https://images.pexels.com/photos/4483772/pexels-photo-4483772.jpeg?auto=compress&cs=tinysrgb&w=1920") center/cover fixed no-repeat;
      color: var(--white);
    }

    .impact-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 80px;
      align-items: center;
    }

    .impact .section-title {
      color: var(--white);
    }

    .stats-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 30px;
    }

    .stat-card {
      border: 1px solid var(--line-dark);
      border-radius: var(--radius);
      padding: 48px 40px;
      background: var(--glass-dark);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      transition: border-color 0.4s ease;
    }
    
    .stat-card:hover {
      border-color: var(--orange);
    }

    .stat-card strong {
      display: block;
      color: var(--orange);
      font-size: clamp(3.5rem, 4vw, 4.5rem);
      line-height: 1;
      font-weight: 800;
    }

    .stat-card span {
      display: block;
      margin-top: 16px;
      color: var(--white);
      font-weight: 600;
      font-size: 1.15rem;
      letter-spacing: 0.05em;
    }

    .reviews {
      background: var(--bg-sec);
      border-top: 1px solid var(--line);
    }

    .review-shell {
      position: relative;
      margin-top: 60px;
      overflow: hidden;
    }

    .review-track {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 40px;
      transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .review-card {
      border: 1px solid var(--line);
      border-radius: var(--radius);
      padding: 48px 40px;
      background: var(--white);
      box-shadow: var(--shadow);
    }

    .stars {
      display: flex;
      gap: 6px;
      color: var(--orange);
      font-size: 1.2rem;
    }

    .review-card p {
      margin-top: 32px;
      color: var(--charcoal);
      font-size: 1.2rem;
      font-weight: 400;
      line-height: 1.8;
    }

    .reviewer {
      margin-top: 40px;
      padding-top: 32px;
      border-top: 1px solid var(--line);
    }

    .reviewer strong {
      display: block;
      color: var(--charcoal);
      line-height: 1.4;
      font-size: 1.2rem;
      font-weight: 700;
    }

    .reviewer span {
      color: var(--text-muted);
      font-size: 0.95rem;
      font-weight: 500;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .review-dots {
      display: none;
      justify-content: center;
      gap: 12px;
      margin-top: 48px;
    }

    .review-dot {
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: rgba(0, 0, 0, 0.1);
      cursor: pointer;
      transition: all 0.4s ease;
    }

    .review-dot.active {
      width: 40px;
      border-radius: 6px;
      background: var(--orange);
    }

    .clients {
      padding-top: 0;
      background: var(--bg-sec);
    }

    .client-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 30px;
      margin-top: 60px;
    }

    .client-card {
      display: grid;
      min-height: 140px;
      place-items: center;
      border: 1px solid var(--line);
      border-radius: var(--radius-sm);
      background: var(--white);
      color: var(--text-muted);
      font-size: clamp(1.2rem, 2vw, 1.6rem);
      font-weight: 700;
      filter: grayscale(1) opacity(0.6);
      transition: all 0.5s ease;
    }

    .client-card:hover {
      color: var(--charcoal);
      filter: grayscale(0) opacity(1);
      transform: translateY(-8px);
      box-shadow: var(--shadow);
      border-color: var(--orange);
    }

    .cta {
      padding: 160px 0;
      overflow: hidden;
      background: var(--bg-main);
      border-top: 1px solid var(--line);
    }

    .cta-card {
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 60px;
      align-items: center;
      border: 1px solid var(--orange);
      border-radius: var(--radius);
      padding: clamp(60px, 8vw, 100px) clamp(40px, 6vw, 80px);
      background: var(--orange-light);
      box-shadow: var(--shadow-lg);
    }

    .cta h2 {
      color: var(--charcoal);
      font-size: clamp(2.5rem, 4vw, 3.5rem);
      line-height: 1.15;
      font-weight: 800;
    }

    .cta p {
      max-width: 720px;
      margin-top: 24px;
      color: var(--text-main);
      font-size: 1.15rem;
      font-weight: 500;
      line-height: 1.8;
    }

    .cta-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      justify-content: flex-end;
    }

    /* Footer */
    .footer {
      background: var(--bg-dark);
      color: var(--text-muted);
    }

    .footer-top {
      display: grid;
      grid-template-columns: 1.5fr 1fr 1fr;
      gap: 80px;
      padding: 120px 0 80px;
      border-bottom: 1px solid var(--line-dark);
    }

    .footer .brand {
      margin-bottom: 32px;
    }
    
    .footer .brand-logo-plate {
      background: var(--white);
      padding: 12px;
      border-radius: 8px;
    }

    .footer p {
      max-width: 500px;
      font-size: 1.05rem;
      line-height: 1.8;
    }

    .footer h3 {
      margin-bottom: 32px;
      color: var(--white);
      font-size: 1.2rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }

    .footer-links,
    .contact-list {
      display: grid;
      gap: 20px;
      list-style: none;
    }

    .footer-links a,
    .contact-list a {
      transition: color 0.3s ease;
    }

    .footer-links a:hover,
    .contact-list a:hover {
      color: var(--orange);
    }

    .contact-list li {
      display: flex;
      gap: 16px;
      align-items: flex-start;
      line-height: 1.6;
    }

    .contact-list i {
      margin-top: 6px;
      color: var(--orange);
    }

    .footer-bottom {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
      padding: 40px 0;
      font-size: 0.95rem;
    }

    .footer-socials {
      display: flex;
      gap: 16px;
    }
    
    .footer-socials a {
      display: inline-flex;
      width: 44px;
      height: 44px;
      align-items: center;
      justify-content: center;
      border: 1px solid var(--line-dark);
      border-radius: 50%;
      color: var(--text-muted);
      transition: all 0.3s ease;
    }
    
    .footer-socials a:hover {
      border-color: var(--orange);
      background: var(--orange);
      color: var(--white);
      transform: translateY(-4px);
    }

    .reveal {
      opacity: 0;
      transform: translateY(40px);
      transition: opacity 1s cubic-bezier(0.16, 1, 0.3, 1), transform 1s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .reveal.visible {
      opacity: 1;
      transform: translateY(0);
    }

    @keyframes heroIn {
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    @keyframes floatGlow {
      0%, 100% { transform: translate3d(0, 0, 0) scale(1); }
      50% { transform: translate3d(-30px, -30px, 0) scale(1.1); }
    }

    @keyframes floatPanel {
      0%, 100% { transform: translate3d(0, 0, 0); }
      50% { transform: translate3d(0, -20px, 0); }
    }

    @keyframes scrollLine {
      0%, 100% { transform: scaleY(0.3); transform-origin: top; }
      50% { transform: scaleY(1); transform-origin: bottom; }
    }

    @media (max-width: 1280px) {
      .nav-menu {
        gap: 24px;
      }

      .socials {
        display: none;
      }

      .sector-grid {
        grid-template-columns: repeat(4, 1fr);
      }

      .why-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    @media (max-width: 920px) {
      .container {
        width: min(100% - 40px, var(--container));
      }

      .menu-toggle {
        display: grid;
      }

      .nav-menu {
        position: fixed;
        top: 100px;
        right: 20px;
        left: 20px;
        display: grid;
        gap: 0;
        padding: 24px;
        border: 1px solid var(--line);
        border-radius: var(--radius);
        background: var(--white);
        box-shadow: var(--shadow-lg);
        opacity: 0;
        pointer-events: none;
        transform: translateY(-16px);
        transition: opacity 0.4s ease, transform 0.4s ease;
      }

      .nav-menu.open {
        opacity: 1;
        pointer-events: auto;
        transform: translateY(0);
      }

      .site-header.scrolled .nav-menu {
        top: 76px;
      }

      .nav-link {
        padding: 16px;
        font-size: 1.1rem;
      }

      .nav-actions .btn {
        display: none;
      }

      .hero {
        min-height: auto;
        padding-top: 160px;
      }

      .hero-inner {
        grid-template-columns: 1fr;
      }

      .hero-copy {
        max-width: 100%;
      }

      .hero-visual {
        min-height: 480px;
        max-width: 700px;
        margin: 60px auto 0;
      }

      .hero-metrics,
      .product-grid,
      .about-grid,
      .impact-grid,
      .cta-card,
      .footer-top {
        grid-template-columns: 1fr;
      }

      .hero-metrics,
      .stats-grid,
      .feature-grid,
      .client-grid,
      .capability-grid {
        grid-template-columns: repeat(2, 1fr);
      }

      .capability-item:nth-child(2) {
        border-right: 0;
      }

      .section-head {
        display: block;
      }

      .section-head .section-subtitle {
        margin-top: 24px;
      }

      .about-grid {
        gap: 60px;
      }

      .image-frame img {
        min-height: 400px;
      }

      .sector-grid {
        grid-template-columns: repeat(3, 1fr);
      }

      .review-track {
        display: flex;
        gap: 0;
      }

      .review-card {
        flex: 0 0 100%;
      }

      .review-dots {
        display: flex;
      }

      .cta-actions {
        justify-content: flex-start;
      }
    }

    @media (max-width: 640px) {
      .section-pad {
        padding: 100px 0;
      }

      .nav {
        height: 80px;
      }

      .site-header.scrolled .nav {
        height: 70px;
      }

      .brand-logo-plate {
        height: 40px;
      }

      .nav-menu {
        top: 80px;
      }

      .site-header.scrolled .nav-menu {
        top: 70px;
      }

      .hero {
        padding: 120px 0 60px;
      }

      .hero-visual {
        min-height: 380px;
      }

      .main-visual {
        inset: 20px 0 20px 0;
      }

      .floating-panel {
        min-width: 200px;
        padding: 16px;
      }

      .panel-bottom {
        right: 0;
      }

      .hero-badge {
        align-items: flex-start;
      }

      .hero h1 {
        font-size: clamp(2.8rem, 10vw, 3.8rem);
      }

      .hero-ctas,
      .cta-actions {
        display: grid;
      }

      .btn {
        width: 100%;
      }

      .hero-metrics,
      .stats-grid,
      .feature-grid,
      .sector-grid,
      .why-grid,
      .client-grid,
      .capability-grid {
        grid-template-columns: 1fr;
      }

      .capability-band {
        margin-top: -40px;
      }

      .capability-item {
        min-height: auto;
        border-right: 0;
        border-bottom: 1px solid var(--line);
        padding: 40px 32px;
      }

      .capability-item:last-child {
        border-bottom: 0;
      }

      .metric {
        padding: 24px;
      }

      .scroll-cue {
        display: none;
      }

      .product-media {
        height: 220px;
      }

      .why-card {
        min-height: auto;
      }

      .footer-bottom {
        display: grid;
        gap: 24px;
        text-align: center;
      }
      
      .footer-socials {
        justify-content: center;
      }
    }
"""

with open('/Users/suryateja/Downloads/VCTRL WEBSITE/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace fonts
content = re.sub(
    r'<link href="https://fonts\.googleapis\.com/css2\?family=[^"]*" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">',
    content
)

# Replace <style> block
content = re.sub(
    r'<style>.*?</style>',
    '<style>\n' + css + '\n  </style>',
    content,
    flags=re.DOTALL
)

with open('/Users/suryateja/Downloads/VCTRL WEBSITE/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html successfully with Orange and White Premium theme.")
