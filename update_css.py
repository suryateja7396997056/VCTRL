import re

css = """
    :root {
      --navy: #050505;
      --navy-2: #0a0a0a;
      --charcoal: #111111;
      --orange: #d4af37; /* Gold */
      --orange-2: #f3e5ab; /* Light Gold */
      --orange-3: #aa7c11; /* Dark Gold */
      --cyan: #e5e7eb;
      --white: #ffffff;
      --soft: #1a1a1a;
      --muted: #a1a1aa;
      --line: rgba(212, 175, 55, 0.15);
      --glass: rgba(5, 5, 5, 0.75);
      --shadow: 0 32px 110px rgba(212, 175, 55, 0.08);
      --soft-shadow: 0 24px 70px rgba(0, 0, 0, 0.5);
      --radius: 12px;
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
      background: var(--navy);
    }

    body {
      min-width: 320px;
      overflow-x: hidden;
      background: var(--navy);
      background-image: 
        radial-gradient(circle at 15% 50%, rgba(212, 175, 55, 0.04), transparent 25%),
        radial-gradient(circle at 85% 30%, rgba(212, 175, 55, 0.04), transparent 25%);
      color: var(--white);
      font-family: "Outfit", sans-serif;
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
      color: var(--orange-2);
      font-size: 0.8rem;
      font-weight: 500;
      letter-spacing: 0.25em;
      text-transform: uppercase;
    }

    .eyebrow::before {
      content: "";
      width: 40px;
      height: 1px;
      background: linear-gradient(90deg, var(--orange-2), transparent);
    }

    .section-title {
      color: var(--white);
      font-family: "Cormorant Garamond", serif;
      font-size: clamp(2.5rem, 4vw, 4rem);
      line-height: 1.1;
      letter-spacing: -0.02em;
      font-weight: 500;
    }

    .section-subtitle {
      max-width: 720px;
      margin-top: 24px;
      color: var(--muted);
      font-size: 1.1rem;
      font-weight: 300;
      line-height: 1.8;
    }

    .gradient-text {
      background: linear-gradient(100deg, var(--orange-2) 0%, var(--orange) 50%, var(--orange-3) 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
    }

    .btn {
      position: relative;
      isolation: isolate;
      display: inline-flex;
      min-height: 54px;
      align-items: center;
      justify-content: center;
      gap: 12px;
      padding: 16px 32px;
      border-radius: 4px;
      cursor: pointer;
      font-size: 0.9rem;
      font-weight: 400;
      letter-spacing: 0.1em;
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
      background: rgba(255, 255, 255, 0.1);
      transform: scaleX(0);
      transform-origin: right;
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .btn:hover::before {
      transform: scaleX(1);
      transform-origin: left;
    }

    .btn:hover {
      transform: translateY(-2px);
    }

    .btn-primary {
      background: linear-gradient(135deg, var(--orange), var(--orange-3));
      color: var(--navy);
      border: 1px solid transparent;
      box-shadow: 0 14px 34px rgba(212, 175, 55, 0.15);
      font-weight: 500;
    }

    .btn-primary:hover {
      box-shadow: 0 20px 48px rgba(212, 175, 55, 0.3);
      color: var(--navy);
    }

    .btn-secondary {
      border: 1px solid var(--line);
      background: transparent;
      color: var(--white);
      backdrop-filter: blur(12px);
    }

    .btn-secondary:hover {
      border-color: var(--orange);
      color: var(--orange-2);
    }

    .btn-light {
      border: 1px solid var(--line);
      background: var(--soft);
      color: var(--white);
      box-shadow: 0 14px 35px rgba(0, 0, 0, 0.2);
    }

    .btn-light:hover {
      border-color: var(--orange);
    }

    .icon-button {
      display: inline-grid;
      width: 44px;
      height: 44px;
      place-items: center;
      border: 1px solid var(--line);
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.02);
      color: var(--muted);
      transition: all 0.4s ease;
    }

    .icon-button:hover {
      border-color: var(--orange);
      color: var(--orange-2);
      transform: translateY(-2px);
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
      box-shadow: 0 12px 40px rgba(0, 0, 0, 0.5);
    }

    .nav {
      display: flex;
      height: 90px;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
      transition: height 0.4s ease;
    }

    .site-header.scrolled .nav {
      height: 70px;
    }

    .brand {
      display: inline-flex;
      min-width: max-content;
      align-items: center;
      gap: 12px;
      color: var(--white);
      font-weight: 500;
      letter-spacing: 0;
    }

    .brand-logo-plate {
      display: inline-flex;
      width: 180px;
      height: 54px;
      align-items: center;
      justify-content: center;
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 4px;
      background: rgba(255, 255, 255, 0.96);
      box-shadow: 0 16px 45px rgba(0, 0, 0, 0.4);
      overflow: hidden;
      padding: 8px;
    }

    .brand-logo {
      width: 150px;
      height: auto;
    }

    .brand-mark {
      display: grid;
      width: 44px;
      height: 44px;
      place-items: center;
      border: 1px solid rgba(255, 255, 255, 0.18);
      border-radius: var(--radius);
      background: linear-gradient(145deg, var(--orange-2), var(--orange-3));
      box-shadow: 0 14px 30px rgba(212, 175, 55, 0.2);
      font-family: "Cormorant Garamond", serif;
      font-size: 1.2rem;
      font-weight: 600;
    }

    .brand-text {
      color: var(--white);
      font-size: 1.1rem;
      line-height: 1.2;
    }

    .brand-text.logo-backed {
      display: none;
    }

    .brand-text span {
      display: block;
      color: var(--muted);
      font-size: 0.7rem;
      font-weight: 400;
      letter-spacing: 0.15em;
      text-transform: uppercase;
    }

    .nav-menu {
      display: flex;
      align-items: center;
      gap: 32px;
      color: var(--muted);
      font-size: 0.9rem;
      font-weight: 400;
      letter-spacing: 0.05em;
      text-transform: uppercase;
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
      height: 1px;
      background: var(--orange);
      transform: scaleX(0);
      transform-origin: right;
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .nav-link:hover {
      color: var(--white);
    }

    .nav-link:hover::after {
      transform: scaleX(1);
      transform-origin: left;
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 16px;
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
      border-radius: 4px;
      background: transparent;
      color: var(--white);
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
      background:
        radial-gradient(circle at 78% 36%, rgba(212, 175, 55, 0.08), transparent 40%),
        linear-gradient(90deg, rgba(5, 5, 5, 0.95) 0%, rgba(5, 5, 5, 0.8) 50%, rgba(5, 5, 5, 0.5) 100%),
        url("https://images.pexels.com/photos/257736/pexels-photo-257736.jpeg?auto=compress&cs=tinysrgb&w=1920") center/cover no-repeat;
      color: #fff;
    }

    .hero::before {
      content: "";
      position: absolute;
      inset: 0;
      opacity: 0.15;
      background-image:
        linear-gradient(rgba(212, 175, 55, 0.1) 1px, transparent 1px),
        linear-gradient(90deg, rgba(212, 175, 55, 0.1) 1px, transparent 1px);
      background-size: 100px 100px;
      mask-image: linear-gradient(180deg, #000 0%, transparent 100%);
    }

    .hero::after {
      content: "";
      position: absolute;
      width: 50vw;
      height: 50vw;
      right: -20vw;
      bottom: -25vw;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(212, 175, 55, 0.15), transparent 60%);
      animation: floatGlow 10s ease-in-out infinite;
    }

    .hero-inner {
      position: relative;
      z-index: 2;
      display: grid;
      grid-template-columns: minmax(0, 1.2fr) minmax(360px, 0.8fr);
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
      padding: 10px 16px;
      border: 1px solid var(--line);
      border-radius: 4px;
      background: rgba(255, 255, 255, 0.03);
      color: var(--orange-2);
      font-size: 0.8rem;
      font-weight: 400;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      backdrop-filter: blur(16px);
      opacity: 0;
      transform: translateY(20px);
      animation: heroIn 0.8s ease forwards 0.15s;
    }

    .hero-badge i {
      color: var(--orange);
    }

    .hero h1 {
      max-width: 900px;
      font-family: "Cormorant Garamond", serif;
      font-size: clamp(3.5rem, 6vw, 6.5rem);
      line-height: 1.05;
      font-weight: 500;
      letter-spacing: -0.02em;
      opacity: 0;
      transform: translateY(30px);
      animation: heroIn 1s cubic-bezier(0.16, 1, 0.3, 1) forwards 0.3s;
    }

    .hero p {
      max-width: 720px;
      margin-top: 24px;
      color: var(--muted);
      font-size: clamp(1.1rem, 1.5vw, 1.25rem);
      line-height: 1.8;
      font-weight: 300;
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
      border-radius: 4px;
      background: var(--glass);
      box-shadow: 0 40px 120px rgba(0, 0, 0, 0.8);
      backdrop-filter: blur(24px);
    }

    .main-visual {
      inset: 40px 0 40px 40px;
    }

    .main-visual::before {
      content: "";
      position: absolute;
      inset: 0;
      z-index: 1;
      background:
        linear-gradient(180deg, transparent, rgba(5, 5, 5, 0.9)),
        linear-gradient(90deg, rgba(212, 175, 55, 0.15), transparent 40%);
    }

    .main-visual::after {
      content: "";
      position: absolute;
      inset: 20px;
      z-index: 2;
      border: 1px solid var(--line);
      border-radius: 2px;
      pointer-events: none;
    }

    .main-visual img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      filter: saturate(1.1) contrast(1.1) brightness(0.9);
      transform: scale(1.05);
    }

    .visual-readout {
      position: absolute;
      z-index: 3;
      right: 32px;
      bottom: 32px;
      min-width: 200px;
      border: 1px solid var(--line);
      border-radius: 4px;
      padding: 24px;
      background: rgba(5, 5, 5, 0.85);
      backdrop-filter: blur(24px);
    }

    .visual-readout span,
    .floating-panel span {
      display: block;
      color: var(--muted);
      font-size: 0.8rem;
      font-weight: 500;
      letter-spacing: 0.1em;
      text-transform: uppercase;
    }

    .visual-readout strong,
    .floating-panel strong {
      display: block;
      margin-top: 8px;
      color: var(--orange-2);
      font-family: "Cormorant Garamond", serif;
      font-size: 2.5rem;
      line-height: 1;
      font-weight: 500;
    }

    .floating-panel {
      position: absolute;
      z-index: 4;
      display: grid;
      grid-template-columns: 48px auto;
      column-gap: 16px;
      align-items: center;
      min-width: 240px;
      border: 1px solid var(--line);
      border-radius: 4px;
      padding: 20px 24px;
      background: rgba(5, 5, 5, 0.85);
      box-shadow: 0 30px 80px rgba(0, 0, 0, 0.6);
      backdrop-filter: blur(24px);
      animation: floatPanel 6s ease-in-out infinite;
    }

    .floating-panel i {
      display: grid;
      width: 48px;
      height: 48px;
      grid-row: span 2;
      place-items: center;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--orange), var(--orange-3));
      color: var(--navy);
      box-shadow: 0 12px 28px rgba(212, 175, 55, 0.2);
      font-size: 1.2rem;
    }

    .floating-panel strong {
      font-size: 1.8rem;
    }

    .panel-top {
      top: 0;
      left: 0;
    }

    .panel-bottom {
      right: -20px;
      bottom: 0;
      animation-delay: 0.8s;
    }

    .metric {
      border: 1px solid var(--line);
      border-radius: 4px;
      padding: 20px;
      background: rgba(255, 255, 255, 0.02);
      backdrop-filter: blur(16px);
      transition: border-color 0.3s ease;
    }
    .metric:hover {
      border-color: var(--orange);
    }

    .metric strong {
      display: block;
      color: var(--orange-2);
      font-family: "Cormorant Garamond", serif;
      font-size: clamp(1.5rem, 2vw, 2rem);
      line-height: 1.1;
      font-weight: 500;
    }

    .metric span {
      display: block;
      margin-top: 8px;
      color: var(--muted);
      font-size: 0.8rem;
      font-weight: 400;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .tech-line {
      position: absolute;
      z-index: 1;
      width: 300px;
      height: 120px;
      right: 10%;
      top: 30%;
      border-top: 1px solid rgba(212, 175, 55, 0.3);
      border-right: 1px solid rgba(212, 175, 55, 0.1);
      opacity: 0.8;
      animation: floatPanel 8s ease-in-out infinite;
    }

    .tech-line::before,
    .tech-line::after {
      content: "";
      position: absolute;
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: var(--orange-2);
      box-shadow: 0 0 0 10px rgba(212, 175, 55, 0.15), 0 0 30px rgba(212, 175, 55, 0.8);
      animation: pulse 2.5s ease-in-out infinite;
    }

    .tech-line::before {
      top: -6px;
      left: 0;
    }

    .tech-line::after {
      right: -6px;
      bottom: 0;
      animation-delay: 1s;
    }

    .scroll-cue {
      position: absolute;
      z-index: 3;
      right: 40px;
      bottom: 40px;
      display: flex;
      align-items: center;
      gap: 16px;
      color: var(--muted);
      font-size: 0.8rem;
      font-weight: 400;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      writing-mode: vertical-rl;
    }

    .scroll-cue span {
      width: 1px;
      height: 60px;
      background: linear-gradient(180deg, rgba(212, 175, 55, 0), rgba(212, 175, 55, 1));
      animation: scrollLine 2s ease-in-out infinite;
    }

    .capability-band {
      position: relative;
      z-index: 5;
      margin-top: -60px;
    }

    .capability-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      border: 1px solid var(--line);
      border-radius: 4px;
      overflow: hidden;
      background: var(--glass);
      box-shadow: 0 40px 100px rgba(0, 0, 0, 0.6);
      backdrop-filter: blur(24px);
    }

    .capability-item {
      min-height: 180px;
      padding: 40px 32px;
      border-right: 1px solid var(--line);
      background: linear-gradient(135deg, rgba(212, 175, 55, 0.05), transparent);
      transition: background 0.4s ease;
    }

    .capability-item:hover {
      background: linear-gradient(135deg, rgba(212, 175, 55, 0.15), transparent);
    }

    .capability-item:last-child {
      border-right: 0;
    }

    .capability-item i {
      color: var(--orange);
      font-size: 1.8rem;
    }

    .capability-item h3 {
      margin-top: 24px;
      color: var(--white);
      font-family: "Cormorant Garamond", serif;
      font-size: 1.6rem;
      font-weight: 500;
      line-height: 1.2;
    }

    .capability-item p {
      margin-top: 12px;
      color: var(--muted);
      font-size: 0.95rem;
      line-height: 1.6;
      font-weight: 300;
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
      border-radius: 4px;
      overflow: hidden;
      box-shadow: 0 40px 100px rgba(0, 0, 0, 0.6);
    }

    .image-frame::before {
      content: "";
      position: absolute;
      inset: 24px;
      z-index: 1;
      border: 1px solid rgba(212, 175, 55, 0.4);
      border-radius: 2px;
      pointer-events: none;
    }

    .image-frame::after {
      content: "";
      position: absolute;
      inset: auto 0 0;
      height: 50%;
      background: linear-gradient(0deg, rgba(5, 5, 5, 0.9), transparent);
    }

    .image-frame img {
      width: 100%;
      min-height: 600px;
      object-fit: cover;
      transform: scale(1.05);
      filter: brightness(0.85);
    }

    .about-copy > p {
      margin-top: 24px;
      color: var(--muted);
      font-size: 1.1rem;
      font-weight: 300;
      line-height: 1.8;
    }

    .feature-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      margin: 40px 0;
    }

    .feature-card,
    .why-card,
    .product-card,
    .review-card,
    .client-card {
      border-radius: 4px;
      transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .feature-card {
      border: 1px solid var(--line);
      padding: 24px;
      background: rgba(255, 255, 255, 0.02);
      box-shadow: 0 14px 36px rgba(0, 0, 0, 0.2);
    }

    .feature-card i {
      display: grid;
      width: 48px;
      height: 48px;
      place-items: center;
      border-radius: 4px;
      background: rgba(212, 175, 55, 0.1);
      color: var(--orange);
      font-size: 1.2rem;
    }

    .feature-card h3 {
      margin-top: 20px;
      color: var(--white);
      font-size: 1.1rem;
      font-weight: 400;
      line-height: 1.3;
      font-family: "Cormorant Garamond", serif;
    }

    .feature-card:hover {
      transform: translateY(-8px);
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.4);
      border-color: var(--orange);
    }

    .products {
      background: var(--navy-2);
      border-top: 1px solid var(--line);
      border-bottom: 1px solid var(--line);
      overflow: hidden;
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
      gap: 30px;
    }

    .product-card {
      position: relative;
      overflow: hidden;
      border: 1px solid var(--line);
      background: var(--navy);
      box-shadow: 0 16px 46px rgba(0, 0, 0, 0.3);
    }

    .product-media {
      position: relative;
      height: 260px;
      overflow: hidden;
      background: var(--navy-2);
    }

    .product-media::after {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(0deg, rgba(5, 5, 5, 0.9), rgba(5, 5, 5, 0.1));
    }

    .product-media img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), filter 0.6s ease;
      filter: brightness(0.85);
    }

    .product-body {
      padding: 32px;
    }

    .product-body h3 {
      color: var(--white);
      font-family: "Cormorant Garamond", serif;
      font-size: 1.8rem;
      line-height: 1.2;
      font-weight: 500;
    }

    .product-body p {
      margin-top: 16px;
      color: var(--muted);
      font-size: 1rem;
      font-weight: 300;
      line-height: 1.6;
    }

    .micro-cta {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      margin-top: 24px;
      color: var(--orange-2);
      font-size: 0.9rem;
      font-weight: 400;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      transition: gap 0.3s ease;
    }

    .product-card:hover {
      border-color: var(--orange);
      box-shadow: 0 24px 60px rgba(212, 175, 55, 0.15), 0 20px 48px rgba(0, 0, 0, 0.4);
      transform: translateY(-8px);
    }

    .product-card:hover img {
      filter: brightness(1);
      transform: scale(1.1);
    }
    
    .product-card:hover .micro-cta {
      gap: 16px;
      color: var(--orange);
    }

    .dark-section {
      overflow: hidden;
      background: var(--navy);
      color: var(--white);
    }

    .dark-section::before {
      content: "";
      position: absolute;
      inset: 0;
      opacity: 0.15;
      background-image:
        linear-gradient(rgba(212, 175, 55, 0.1) 1px, transparent 1px),
        linear-gradient(90deg, rgba(212, 175, 55, 0.1) 1px, transparent 1px);
      background-size: 100px 100px;
    }

    .dark-section .container {
      position: relative;
      z-index: 1;
    }

    .sector-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 20px;
      margin-top: 60px;
    }

    .sector-card {
      display: flex;
      min-height: 90px;
      align-items: center;
      gap: 16px;
      border: 1px solid var(--line);
      border-radius: 4px;
      padding: 20px;
      background: rgba(255, 255, 255, 0.02);
      color: var(--muted);
      font-size: 1rem;
      font-weight: 300;
      backdrop-filter: blur(12px);
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .sector-card i {
      flex: 0 0 auto;
      color: var(--orange);
      font-size: 1.2rem;
    }

    .sector-card:hover {
      border-color: var(--orange);
      background: rgba(212, 175, 55, 0.05);
      color: var(--white);
      box-shadow: 0 16px 42px rgba(212, 175, 55, 0.1);
      transform: translateY(-6px);
    }

    .why-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 30px;
      margin-top: 60px;
    }

    .why-card {
      min-height: 300px;
      border: 1px solid var(--line);
      padding: 40px;
      background: var(--navy-2);
      box-shadow: 0 16px 46px rgba(0, 0, 0, 0.3);
    }

    .why-card i {
      display: grid;
      width: 64px;
      height: 64px;
      place-items: center;
      border-radius: 50%;
      border: 1px solid var(--orange);
      background: transparent;
      color: var(--orange);
      font-size: 1.5rem;
      transition: all 0.4s ease;
    }

    .why-card h3 {
      margin-top: 32px;
      color: var(--white);
      font-family: "Cormorant Garamond", serif;
      font-size: 1.8rem;
      line-height: 1.2;
      font-weight: 500;
    }

    .why-card p {
      margin-top: 16px;
      color: var(--muted);
      font-size: 1rem;
      font-weight: 300;
      line-height: 1.6;
    }

    .why-card:hover {
      border-color: var(--orange);
      transform: translateY(-8px);
      box-shadow: 0 30px 80px rgba(0, 0, 0, 0.5);
    }
    
    .why-card:hover i {
      background: var(--orange);
      color: var(--navy);
    }

    .impact {
      padding: 160px 0;
      background:
        linear-gradient(90deg, rgba(5, 5, 5, 0.95), rgba(5, 5, 5, 0.8)),
        url("https://images.pexels.com/photos/4483772/pexels-photo-4483772.jpeg?auto=compress&cs=tinysrgb&w=1920") center/cover fixed no-repeat;
      color: var(--white);
    }

    .impact-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 60px;
      align-items: center;
    }

    .stats-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 24px;
    }

    .stat-card {
      border: 1px solid var(--line);
      border-radius: 4px;
      padding: 40px 32px;
      background: var(--glass);
      backdrop-filter: blur(24px);
      transition: border-color 0.4s ease;
    }
    
    .stat-card:hover {
      border-color: var(--orange);
    }

    .stat-card strong {
      display: block;
      color: var(--orange);
      font-family: "Cormorant Garamond", serif;
      font-size: clamp(3rem, 4vw, 4rem);
      line-height: 1;
      font-weight: 500;
    }

    .stat-card span {
      display: block;
      margin-top: 16px;
      color: var(--white);
      font-weight: 400;
      font-size: 1.1rem;
      letter-spacing: 0.05em;
    }

    .reviews {
      background: var(--navy-2);
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
      gap: 30px;
      transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .review-card {
      border: 1px solid var(--line);
      padding: 40px;
      background: var(--navy);
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    }

    .stars {
      display: flex;
      gap: 6px;
      color: var(--orange);
      font-size: 1rem;
    }

    .review-card p {
      margin-top: 24px;
      color: var(--white);
      font-size: 1.15rem;
      font-style: italic;
      font-weight: 300;
      line-height: 1.8;
    }

    .reviewer {
      margin-top: 32px;
      padding-top: 24px;
      border-top: 1px solid var(--line);
    }

    .reviewer strong {
      display: block;
      color: var(--orange-2);
      line-height: 1.4;
      font-size: 1.1rem;
      font-weight: 500;
    }

    .reviewer span {
      color: var(--muted);
      font-size: 0.9rem;
      font-weight: 400;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }

    .review-dots {
      display: none;
      justify-content: center;
      gap: 12px;
      margin-top: 40px;
    }

    .review-dot {
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.1);
      cursor: pointer;
      transition: all 0.4s ease;
    }

    .review-dot.active {
      width: 32px;
      border-radius: 6px;
      background: var(--orange);
    }

    .clients {
      padding-top: 0;
      background: var(--navy-2);
    }

    .client-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 24px;
      margin-top: 60px;
    }

    .client-card {
      display: grid;
      min-height: 120px;
      place-items: center;
      border: 1px solid var(--line);
      background: transparent;
      color: var(--muted);
      font-family: "Cormorant Garamond", serif;
      font-size: clamp(1.2rem, 2vw, 1.6rem);
      font-weight: 500;
      filter: grayscale(1) opacity(0.5);
      transition: all 0.5s ease;
    }

    .client-card:hover {
      color: var(--orange-2);
      filter: grayscale(0) opacity(1);
      transform: translateY(-8px);
      box-shadow: 0 26px 60px rgba(0, 0, 0, 0.4);
      border-color: var(--orange);
    }

    .cta {
      padding: 160px 0;
      overflow: hidden;
      background: var(--navy);
      border-top: 1px solid var(--line);
      color: var(--white);
    }

    .cta-card {
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 40px;
      align-items: center;
      border: 1px solid var(--orange);
      border-radius: 4px;
      padding: clamp(40px, 6vw, 80px) clamp(40px, 6vw, 60px);
      background: linear-gradient(135deg, rgba(212, 175, 55, 0.1), transparent);
      box-shadow: 0 40px 100px rgba(0, 0, 0, 0.6);
    }

    .cta h2 {
      font-family: "Cormorant Garamond", serif;
      font-size: clamp(2.5rem, 4vw, 4rem);
      line-height: 1.1;
      font-weight: 500;
    }

    .cta p {
      max-width: 720px;
      margin-top: 20px;
      color: var(--muted);
      font-size: 1.1rem;
      font-weight: 300;
      line-height: 1.8;
    }

    .cta-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
      justify-content: flex-end;
    }

    /* Footer */
    .footer {
      background: #000;
      color: var(--muted);
      border-top: 1px solid var(--line);
    }

    .footer-top {
      display: grid;
      grid-template-columns: 1.5fr 1fr 1fr;
      gap: 60px;
      padding: 100px 0 60px;
      border-bottom: 1px solid var(--line);
    }

    .footer .brand {
      margin-bottom: 24px;
    }

    .footer p {
      max-width: 500px;
      font-size: 1rem;
      font-weight: 300;
      line-height: 1.8;
    }

    .footer h3 {
      margin-bottom: 24px;
      color: var(--white);
      font-size: 1.1rem;
      font-weight: 500;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      font-family: "Cormorant Garamond", serif;
    }

    .footer-links,
    .contact-list {
      display: grid;
      gap: 16px;
      list-style: none;
    }

    .footer-links a,
    .contact-list a {
      font-weight: 300;
      transition: color 0.3s ease;
    }

    .footer-links a:hover,
    .contact-list a:hover {
      color: var(--orange-2);
    }

    .contact-list li {
      display: flex;
      gap: 16px;
      align-items: flex-start;
      font-weight: 300;
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
      gap: 20px;
      padding: 32px 0;
      font-size: 0.9rem;
      font-weight: 300;
    }

    .footer-socials {
      display: flex;
      gap: 12px;
    }
    
    .footer-socials a {
      display: inline-flex;
      width: 36px;
      height: 36px;
      align-items: center;
      justify-content: center;
      border: 1px solid var(--line);
      border-radius: 50%;
      color: var(--muted);
      transition: all 0.3s ease;
    }
    
    .footer-socials a:hover {
      border-color: var(--orange);
      color: var(--orange-2);
      transform: translateY(-2px);
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

    @keyframes pulse {
      0%, 100% { transform: scale(1); opacity: 0.8; }
      50% { transform: scale(1.5); opacity: 1; }
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
        top: 90px;
        right: 20px;
        left: 20px;
        display: grid;
        gap: 0;
        padding: 20px;
        border: 1px solid var(--line);
        border-radius: 4px;
        background: var(--glass);
        box-shadow: 0 40px 100px rgba(0, 0, 0, 0.8);
        backdrop-filter: blur(24px);
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
        top: 70px;
      }

      .nav-link {
        padding: 16px;
        font-size: 1rem;
      }

      .nav-actions .btn {
        display: none;
      }

      .hero {
        min-height: auto;
        padding-top: 140px;
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
        margin: 40px auto 0;
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

      .capability-grid {
        border-radius: 4px;
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

      .brand-mark {
        width: 40px;
        height: 40px;
      }

      .brand-logo-plate {
        width: 140px;
        height: 44px;
      }

      .brand-logo {
        width: 120px;
      }

      .brand-text {
        font-size: 1rem;
      }

      .brand-text span {
        font-size: 0.6rem;
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
        font-size: 0.75rem;
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
        padding: 32px 24px;
      }

      .capability-item:last-child {
        border-bottom: 0;
      }

      .metric {
        padding: 24px;
      }

      .tech-line,
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
    r'<link href="https://fonts\.googleapis\.com/css2\?family=Inter[^"]*" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600&family=Cormorant+Garamond:wght@400;500;600;700&display=swap" rel="stylesheet">',
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

print("Updated index.html successfully.")
