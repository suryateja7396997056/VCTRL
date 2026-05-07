import re

def update_file(filename, new_main):
    with open(filename, "r") as f:
        content = f.read()
    content = re.sub(r'<main>.*?</main>', new_main, content, flags=re.DOTALL)
    with open(filename, "w") as f:
        f.write(content)

about_main = """  <main>
    <section class="hero" style="min-height: 50vh; padding-top: 150px; padding-bottom: 80px;">
      <div class="tech-line" aria-hidden="true"></div>
      <div class="container hero-inner" style="grid-template-columns: 1fr;">
        <div class="hero-copy" style="text-align: center;">
          <div class="hero-badge"><i class="fa-solid fa-building"></i> Company Profile</div>
          <h1 style="font-size: 3.5rem;">About <span class="gradient-text">V-Ctrl Solutions</span></h1>
          <p style="margin: 0 auto; max-width: 700px;">We believe that delivering the right power solution begins with people. Technology and innovation are fundamental pillars for us.</p>
        </div>
      </div>
    </section>

    <section class="section-pad">
      <div class="container" style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: center;">
        <div class="product-media" style="height: auto;">
          <img src="https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Team Discussion" style="width: 100%; border-radius: 12px; box-shadow: var(--shadow-lg);">
        </div>
        <div>
          <span class="eyebrow">Our Story</span>
          <h2 style="font-size: 2.5rem; margin-bottom: 24px; color: var(--text-dark);">25+ Years of Excellence</h2>
          <p style="color: var(--text-light); line-height: 1.8; margin-bottom: 16px;">V-Ctrl was started with a mission to provide total turnkey solutions in power conditioning and energy-saving products, representing a cohesive integration of consultancy, design, manufacturing, installation, and maintenance services based on its founder’s experience of over 25+ years.</p>
          <p style="color: var(--text-light); line-height: 1.8; margin-bottom: 24px;">Our team consists of industry experts with years of hands-on industrial electrical and onsite experience. We value performance, passion, and knowledge, and it is from this foundation that we set industry standards in equipment selection, project design, and customer service.</p>
          <div class="hero-metrics" aria-label="Company trust metrics" style="margin-top: 24px;">
            <div class="metric"><strong>25+</strong><span>Years</span></div>
            <div class="metric"><strong>10k+</strong><span>Clients</span></div>
            <div class="metric"><strong>847+</strong><span>Projects</span></div>
          </div>
        </div>
      </div>
    </section>

    <section class="section-pad dark-section">
      <div class="container">
        <div class="reveal" style="text-align: center; margin-bottom: 48px;">
          <span class="eyebrow">Why Choose Us</span>
          <h2 class="section-title">The V-Ctrl Advantage</h2>
        </div>
        <div class="why-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px;">
          <div class="why-card reveal">
            <div class="why-icon"><i class="fa-solid fa-industry"></i></div>
            <h3>Manufacturing Potential</h3>
            <p>We are the only manufacturers in South India with the potential to design and manufacture power distribution units of any capacity.</p>
          </div>
          <div class="why-card reveal" style="transition-delay: 100ms;">
            <div class="why-icon"><i class="fa-solid fa-microscope"></i></div>
            <h3>100% Testing Capability</h3>
            <p>We have 100 per cent testing capability and infrastructure as per industry standards ensuring zero defects.</p>
          </div>
          <div class="why-card reveal" style="transition-delay: 200ms;">
            <div class="why-icon"><i class="fa-solid fa-handshake"></i></div>
            <h3>Prestigious Institutions</h3>
            <p>Through best-in-the-market products and services, we have been the favorite pick to institutions like Megha Engineering, ISRO, Tata Motors.</p>
          </div>
        </div>
      </div>
    </section>
  </main>"""

services_main = """  <main>
    <section class="hero" style="min-height: 50vh; padding-top: 150px; padding-bottom: 80px;">
      <div class="tech-line" aria-hidden="true"></div>
      <div class="container hero-inner" style="grid-template-columns: 1fr;">
        <div class="hero-copy" style="text-align: center;">
          <div class="hero-badge"><i class="fa-solid fa-tools"></i> Expert Solutions</div>
          <h1 style="font-size: 3.5rem;">Our <span class="gradient-text">Services</span></h1>
          <p style="margin: 0 auto; max-width: 700px;">Comprehensive installation, maintenance, and consulting services to ensure your power infrastructure operates flawlessly.</p>
        </div>
      </div>
    </section>

    <section class="section-pad">
      <div class="container">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 48px;">
          
          <div class="reveal" style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 16px; overflow: hidden; box-shadow: var(--shadow-sm);">
            <img src="https://images.pexels.com/photos/1216589/pexels-photo-1216589.jpeg?auto=compress&cs=tinysrgb&w=600" alt="Consultancy" style="width: 100%; height: 200px; object-fit: cover;">
            <div style="padding: 32px;">
              <h3 style="font-size: 1.5rem; color: var(--text-dark); margin-bottom: 16px;">Power Consultancy</h3>
              <p style="color: var(--text-light); line-height: 1.6;">Expert analysis of your facility's power requirements, harmonic distortions, and voltage fluctuations. We recommend the precise equipment needed to safeguard your infrastructure.</p>
            </div>
          </div>

          <div class="reveal" style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 16px; overflow: hidden; box-shadow: var(--shadow-sm); transition-delay: 100ms;">
            <img src="https://images.pexels.com/photos/585419/pexels-photo-585419.jpeg?auto=compress&cs=tinysrgb&w=600" alt="Installation" style="width: 100%; height: 200px; object-fit: cover;">
            <div style="padding: 32px;">
              <h3 style="font-size: 1.5rem; color: var(--text-dark); margin-bottom: 16px;">Turnkey Installation</h3>
              <p style="color: var(--text-light); line-height: 1.6;">Professional onsite installation of Servo Stabilizers, UPS systems, and Isolation Transformers ensuring compliance with the highest industrial safety standards.</p>
            </div>
          </div>

          <div class="reveal" style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 16px; overflow: hidden; box-shadow: var(--shadow-sm); transition-delay: 200ms;">
            <img src="https://images.pexels.com/photos/3862130/pexels-photo-3862130.jpeg?auto=compress&cs=tinysrgb&w=600" alt="Maintenance" style="width: 100%; height: 200px; object-fit: cover;">
            <div style="padding: 32px;">
              <h3 style="font-size: 1.5rem; color: var(--text-dark); margin-bottom: 16px;">Preventive Maintenance</h3>
              <p style="color: var(--text-light); line-height: 1.6;">24/7 dedicated support and regular health checks to prevent sudden power failures. Our AMC services guarantee maximum uptime for your critical operations.</p>
            </div>
          </div>

        </div>
      </div>
    </section>

    <section class="cta" id="contact">
      <div class="container">
        <div class="cta-card reveal">
          <div>
            <h2>Ready to upgrade your power infrastructure?</h2>
            <p>Our engineers are available for immediate onsite inspections and consultations.</p>
          </div>
          <div class="cta-actions">
            <a class="btn btn-primary" href="contact.html">Book a Consultation</a>
          </div>
        </div>
      </div>
    </section>
  </main>"""

sectors_main = """  <main>
    <section class="hero" style="min-height: 50vh; padding-top: 150px; padding-bottom: 80px;">
      <div class="tech-line" aria-hidden="true"></div>
      <div class="container hero-inner" style="grid-template-columns: 1fr;">
        <div class="hero-copy" style="text-align: center;">
          <div class="hero-badge"><i class="fa-solid fa-industry"></i> Wide Presence</div>
          <h1 style="font-size: 3.5rem;">Sectors We <span class="gradient-text">Serve</span></h1>
          <p style="margin: 0 auto; max-width: 700px;">From healthcare to heavy manufacturing, we deliver uncompromised power stability across diverse industrial sectors.</p>
        </div>
      </div>
    </section>

    <section class="section-pad">
      <div class="container">
        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 24px;">
          <!-- Generating Sector Cards -->
          """ + "".join([f"""
          <div class="why-card reveal" style="text-align: center; padding: 32px 24px;">
            <div class="why-icon" style="margin: 0 auto 16px;"><i class="fa-solid fa-{icon}"></i></div>
            <h3 style="font-size: 1.25rem;">{sector}</h3>
          </div>""" for sector, icon in [("Automotive", "car"), ("Buildings & Infra", "city"), ("Cement", "trowel-bricks"), ("IT & Data Centers", "server"), ("Hospitality", "hotel"), ("Healthcare", "hospital"), ("Pharmaceutical", "pills"), ("Food & Beverage", "utensils"), ("Oil & Gas", "oil-well"), ("Smart Cities", "network-wired")]]) + """
        </div>
      </div>
    </section>
  </main>"""

clients_main = """  <main>
    <section class="hero" style="min-height: 50vh; padding-top: 150px; padding-bottom: 80px;">
      <div class="tech-line" aria-hidden="true"></div>
      <div class="container hero-inner" style="grid-template-columns: 1fr;">
        <div class="hero-copy" style="text-align: center;">
          <div class="hero-badge"><i class="fa-solid fa-users"></i> Our Network</div>
          <h1 style="font-size: 3.5rem;">Our <span class="gradient-text">Clients</span></h1>
          <p style="margin: 0 auto; max-width: 700px;">Over 10,000 happy clients trust V-Ctrl Solutions to safeguard their critical machinery and IT infrastructure.</p>
        </div>
      </div>
    </section>

    <section class="section-pad dark-section" id="clients">
      <div class="container">
        <div class="reveal" style="text-align: center; margin-bottom: 48px;">
          <span class="eyebrow">Prestigious Partners</span>
          <h2 class="section-title">Trusted by Leading Organizations</h2>
        </div>
        <div class="client-grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 24px;">
          <div class="client-card reveal">CBRE</div>
          <div class="client-card reveal">DGS</div>
          <div class="client-card reveal">ELGI</div>
          <div class="client-card reveal">JLL</div>
          <div class="client-card reveal">Yashoda Hospitals</div>
          <div class="client-card reveal">Megha Engineering</div>
          <div class="client-card reveal">ISRO</div>
          <div class="client-card reveal">Tata Motors</div>
          <div class="client-card reveal">Jindal Steels</div>
          <div class="client-card reveal">Dilip Buildcon</div>
        </div>
      </div>
    </section>

    <section class="section-pad reviews">
      <div class="container">
        <div class="reveal" style="text-align: center; margin-bottom: 48px;">
          <span class="eyebrow">Testimonials</span>
          <h2 class="section-title">What Our Clients Say</h2>
        </div>
        
        <div class="review-carousel reveal" style="max-width: 800px; margin: 0 auto;">
          <div class="review-track" id="reviewTrack">
            <div class="review-slide">
              <div class="review-content">
                <i class="fa-solid fa-quote-left" style="color: var(--primary-accent); font-size: 2rem; margin-bottom: 24px;"></i>
                <p>When I search for an oil-cooled transformer for my factory & I got V-Ctrl it is good to take their service. Good service by phone also solved my problem. Very nice. Service... keep it up... delivery also very good. Best Leading Power transformers manufacturers in Hyderabad.</p>
                <div class="author">
                  <strong>Ravi teja Tummalacherla</strong>
                  <span>Manager</span>
                </div>
              </div>
            </div>
            
            <div class="review-slide">
              <div class="review-content">
                <i class="fa-solid fa-quote-left" style="color: var(--primary-accent); font-size: 2rem; margin-bottom: 24px;"></i>
                <p>Recently I purchase servo stabilizer from V-Ctrl. Really good working and good condition products they supplies and manufacturer. Many thanks V-Ctrl.</p>
                <div class="author">
                  <strong>Balu Ponnaganti</strong>
                  <span>Manager</span>
                </div>
              </div>
            </div>
            
            <div class="review-slide">
              <div class="review-content">
                <i class="fa-solid fa-quote-left" style="color: var(--primary-accent); font-size: 2rem; margin-bottom: 24px;"></i>
                <p>V-Ctrl provide excellent quality products and services. The company shows empathy towards customers right from before sale to after sale is what I liked the most, Very promot service responce.</p>
                <div class="author">
                  <strong>Manoj Kumar</strong>
                  <span>Manager</span>
                </div>
              </div>
            </div>
          </div>
          
          <div class="review-dots" id="reviewDots">
            <button class="dot active" aria-label="Review 1"></button>
            <button class="dot" aria-label="Review 2"></button>
            <button class="dot" aria-label="Review 3"></button>
          </div>
        </div>
      </div>
    </section>
  </main>"""

contact_main = """  <main>
    <section class="hero" style="min-height: 40vh; padding-top: 150px; padding-bottom: 50px;">
      <div class="tech-line" aria-hidden="true"></div>
      <div class="container hero-inner" style="grid-template-columns: 1fr;">
        <div class="hero-copy" style="text-align: center;">
          <div class="hero-badge"><i class="fa-solid fa-envelope"></i> Get In Touch</div>
          <h1 style="font-size: 3.5rem;">Contact <span class="gradient-text">Us</span></h1>
        </div>
      </div>
    </section>

    <section class="section-pad">
      <div class="container">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px;">
          
          <div class="reveal">
            <h2 style="font-size: 2rem; margin-bottom: 24px; color: var(--text-dark);">Let's discuss your power requirements</h2>
            <p style="color: var(--text-light); margin-bottom: 32px; line-height: 1.6;">Our technical team is ready to assist you with equipment sizing, technical queries, and custom manufacturing requirements.</p>
            
            <div style="display: flex; gap: 24px; margin-bottom: 24px;">
              <div style="width: 48px; height: 48px; background: rgba(255,87,34,0.1); color: var(--primary-accent); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.25rem; flex-shrink: 0;">
                <i class="fa-solid fa-location-dot"></i>
              </div>
              <div>
                <h4 style="color: var(--text-dark); margin-bottom: 8px;">Head Office</h4>
                <p style="color: var(--text-light); line-height: 1.6;">Cherlapally – Rampally – Ghatkesar Rd, Cherlapalli, Secunderabad, Telangana 501301, India</p>
              </div>
            </div>

            <div style="display: flex; gap: 24px; margin-bottom: 24px;">
              <div style="width: 48px; height: 48px; background: rgba(255,87,34,0.1); color: var(--primary-accent); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.25rem; flex-shrink: 0;">
                <i class="fa-solid fa-phone"></i>
              </div>
              <div>
                <h4 style="color: var(--text-dark); margin-bottom: 8px;">Phone</h4>
                <p style="color: var(--text-light); line-height: 1.6;"><a href="tel:+919986501123" style="color: inherit; text-decoration: none;">+91 99865 01123</a><br><a href="tel:+919848001128" style="color: inherit; text-decoration: none;">+91 98480 01128</a></p>
              </div>
            </div>

            <div style="display: flex; gap: 24px; margin-bottom: 24px;">
              <div style="width: 48px; height: 48px; background: rgba(255,87,34,0.1); color: var(--primary-accent); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.25rem; flex-shrink: 0;">
                <i class="fa-solid fa-envelope"></i>
              </div>
              <div>
                <h4 style="color: var(--text-dark); margin-bottom: 8px;">Email</h4>
                <p style="color: var(--text-light); line-height: 1.6;"><a href="mailto:admin@v-ctrl.com" style="color: inherit; text-decoration: none;">admin@v-ctrl.com</a></p>
              </div>
            </div>
          </div>

          <div class="calc-form reveal">
            <h3>Send an Inquiry</h3>
            <form id="contactForm">
              <div class="form-group">
                <label for="name">Full Name</label>
                <input type="text" id="name" class="form-control" required>
              </div>
              <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" class="form-control" required>
              </div>
              <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" class="form-control" required>
              </div>
              <div class="form-group">
                <label for="message">Your Message</label>
                <textarea id="message" class="form-control" rows="4" required></textarea>
              </div>
              <button type="submit" class="btn btn-primary" style="width: 100%;">Submit Inquiry <i class="fa-solid fa-paper-plane"></i></button>
            </form>
          </div>

        </div>
      </div>
    </section>
    
    <section>
        <div style="width: 100%; height: 400px; background: var(--bg-alt); display: flex; align-items: center; justify-content: center;">
            <p style="color: var(--text-light);">Interactive Google Map Embed will be placed here</p>
        </div>
    </section>
  </main>"""

blog_main = """  <main>
    <section class="hero" style="min-height: 40vh; padding-top: 150px; padding-bottom: 50px;">
      <div class="tech-line" aria-hidden="true"></div>
      <div class="container hero-inner" style="grid-template-columns: 1fr;">
        <div class="hero-copy" style="text-align: center;">
          <div class="hero-badge"><i class="fa-solid fa-newspaper"></i> Latest Updates</div>
          <h1 style="font-size: 3.5rem;">Insights & <span class="gradient-text">Blog</span></h1>
          <p style="margin: 0 auto; max-width: 700px;">Stay updated with the latest technological advancements in power conditioning and industry news.</p>
        </div>
      </div>
    </section>

    <section class="section-pad">
      <div class="container">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 32px;">
          
          <div class="reveal" style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 16px; overflow: hidden; box-shadow: var(--shadow-sm); display: flex; flex-direction: column;">
            <img src="https://images.pexels.com/photos/257736/pexels-photo-257736.jpeg?auto=compress&cs=tinysrgb&w=600" alt="Blog 1" style="width: 100%; height: 200px; object-fit: cover;">
            <div style="padding: 24px; flex-grow: 1; display: flex; flex-direction: column;">
              <span style="color: var(--primary-accent); font-size: 0.875rem; font-weight: 600; margin-bottom: 8px; display: block;">Technical</span>
              <h3 style="font-size: 1.25rem; color: var(--text-dark); margin-bottom: 12px; line-height: 1.4;">Understanding Servo Voltage Stabilizers vs Static Stabilizers</h3>
              <p style="color: var(--text-light); line-height: 1.6; margin-bottom: 24px; flex-grow: 1;">Explore the fundamental differences and discover which stabilization technology is best suited for your heavy industrial machinery.</p>
              <a href="#" style="color: var(--primary-color); font-weight: 600; text-decoration: none; display: inline-flex; align-items: center; gap: 8px;">Read Article <i class="fa-solid fa-arrow-right"></i></a>
            </div>
          </div>

          <div class="reveal" style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 16px; overflow: hidden; box-shadow: var(--shadow-sm); display: flex; flex-direction: column; transition-delay: 100ms;">
            <img src="https://images.pexels.com/photos/3862130/pexels-photo-3862130.jpeg?auto=compress&cs=tinysrgb&w=600" alt="Blog 2" style="width: 100%; height: 200px; object-fit: cover;">
            <div style="padding: 24px; flex-grow: 1; display: flex; flex-direction: column;">
              <span style="color: var(--primary-accent); font-size: 0.875rem; font-weight: 600; margin-bottom: 8px; display: block;">Industry Application</span>
              <h3 style="font-size: 1.25rem; color: var(--text-dark); margin-bottom: 12px; line-height: 1.4;">The Critical Role of Isolation Transformers in Medical Facilities</h3>
              <p style="color: var(--text-light); line-height: 1.6; margin-bottom: 24px; flex-grow: 1;">Why healthcare providers and diagnostic centers mandate isolation transformers to protect sensitive equipment and patient safety.</p>
              <a href="#" style="color: var(--primary-color); font-weight: 600; text-decoration: none; display: inline-flex; align-items: center; gap: 8px;">Read Article <i class="fa-solid fa-arrow-right"></i></a>
            </div>
          </div>

          <div class="reveal" style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 16px; overflow: hidden; box-shadow: var(--shadow-sm); display: flex; flex-direction: column; transition-delay: 200ms;">
            <img src="https://images.pexels.com/photos/1216589/pexels-photo-1216589.jpeg?auto=compress&cs=tinysrgb&w=600" alt="Blog 3" style="width: 100%; height: 200px; object-fit: cover;">
            <div style="padding: 24px; flex-grow: 1; display: flex; flex-direction: column;">
              <span style="color: var(--primary-accent); font-size: 0.875rem; font-weight: 600; margin-bottom: 8px; display: block;">Maintenance</span>
              <h3 style="font-size: 1.25rem; color: var(--text-dark); margin-bottom: 12px; line-height: 1.4;">5 Signs Your Industrial UPS System Needs Immediate Servicing</h3>
              <p style="color: var(--text-light); line-height: 1.6; margin-bottom: 24px; flex-grow: 1;">Don't wait for a power failure. Learn the early warning signs of UPS degradation and how preventive maintenance saves millions.</p>
              <a href="#" style="color: var(--primary-color); font-weight: 600; text-decoration: none; display: inline-flex; align-items: center; gap: 8px;">Read Article <i class="fa-solid fa-arrow-right"></i></a>
            </div>
          </div>

        </div>
      </div>
    </section>
  </main>"""

products_main = """  <main>
    <section class="hero" style="min-height: 40vh; padding-top: 150px; padding-bottom: 50px;">
      <div class="tech-line" aria-hidden="true"></div>
      <div class="container hero-inner" style="grid-template-columns: 1fr;">
        <div class="hero-copy" style="text-align: center;">
          <div class="hero-badge"><i class="fa-solid fa-microchip"></i> Complete Equipment Range</div>
          <h1 style="font-size: 3.5rem;">Our <span class="gradient-text">Products</span></h1>
          <p style="margin: 0 auto; max-width: 600px;">Precision engineered for industrial loads, providing continuous voltage stability and protection for your critical machinery.</p>
        </div>
      </div>
    </section>

    <section class="section-pad">
      <div class="container">
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: center; margin-bottom: 80px;" class="reveal">
          <div class="product-media" style="height: auto;">
            <img src="https://images.pexels.com/photos/257736/pexels-photo-257736.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Servo Voltage Stabilizer" style="width: 100%; border-radius: 12px; box-shadow: var(--shadow-lg);">
          </div>
          <div class="product-details">
            <h2 style="font-size: 2.5rem; margin-bottom: 16px; color: var(--text-dark);">Servo Voltage Stabilizers</h2>
            <p style="color: var(--text-light); margin-bottom: 24px; line-height: 1.6;">Oil cooled and air cooled servo voltage stabilizers to protect your valuable CNC machines, industrial motors, and entire plant load from voltage fluctuations.</p>
            <div class="specs-grid" style="display: grid; gap: 16px;">
              <div style="display: flex; justify-content: space-between; padding-bottom: 16px; border-bottom: 1px solid var(--border-color);">
                <span style="color: var(--text-light); font-weight: 500;">Capacity</span>
                <span style="color: var(--text-dark); font-weight: 600;">Up to 2000 kVA</span>
              </div>
              <div style="display: flex; justify-content: space-between; padding-bottom: 16px; border-bottom: 1px solid var(--border-color);">
                <span style="color: var(--text-light); font-weight: 500;">Input Voltage Range</span>
                <span style="color: var(--text-dark); font-weight: 600;">340V - 460V (3-Phase)</span>
              </div>
              <div style="display: flex; justify-content: space-between; padding-bottom: 16px; border-bottom: 1px solid var(--border-color);">
                <span style="color: var(--text-light); font-weight: 500;">Output Voltage</span>
                <span style="color: var(--text-dark); font-weight: 600;">400V ± 1%</span>
              </div>
            </div>
            <div style="margin-top: 32px;">
              <a href="contact.html" class="btn btn-primary">Request Quote</a>
            </div>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: center; margin-bottom: 80px;" class="reveal">
          <div class="product-details" style="order: 2;">
            <h2 style="font-size: 2.5rem; margin-bottom: 16px; color: var(--text-dark);">Isolation Transformers</h2>
            <p style="color: var(--text-light); margin-bottom: 24px; line-height: 1.6;">Ultra-isolation transformers with multiple shielding to block electrical noise, spikes, and transients, ensuring clean power for medical and IT equipment.</p>
            <div class="specs-grid" style="display: grid; gap: 16px;">
              <div style="display: flex; justify-content: space-between; padding-bottom: 16px; border-bottom: 1px solid var(--border-color);">
                <span style="color: var(--text-light); font-weight: 500;">Coupling Capacitance</span>
                <span style="color: var(--text-dark); font-weight: 600;">Less than 0.01 pF</span>
              </div>
              <div style="display: flex; justify-content: space-between; padding-bottom: 16px; border-bottom: 1px solid var(--border-color);">
                <span style="color: var(--text-light); font-weight: 500;">Common Mode Rejection</span>
                <span style="color: var(--text-dark); font-weight: 600;">120 dB</span>
              </div>
              <div style="display: flex; justify-content: space-between; padding-bottom: 16px; border-bottom: 1px solid var(--border-color);">
                <span style="color: var(--text-light); font-weight: 500;">Insulation Resistance</span>
                <span style="color: var(--text-dark); font-weight: 600;">> 1000 Mega Ohms</span>
              </div>
            </div>
            <div style="margin-top: 32px;">
              <a href="contact.html" class="btn btn-primary">Request Quote</a>
            </div>
          </div>
          <div class="product-media" style="height: auto; order: 1;">
            <img src="https://images.pexels.com/photos/159298/gears-cogs-machine-machinery-159298.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Isolation Transformer" style="width: 100%; border-radius: 12px; box-shadow: var(--shadow-lg);">
          </div>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: center;" class="reveal">
          <div class="product-media" style="height: auto;">
            <img src="https://images.pexels.com/photos/1624895/pexels-photo-1624895.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Online UPS System" style="width: 100%; border-radius: 12px; box-shadow: var(--shadow-lg);">
          </div>
          <div class="product-details">
            <h2 style="font-size: 2.5rem; margin-bottom: 16px; color: var(--text-dark);">Online UPS Systems</h2>
            <p style="color: var(--text-light); margin-bottom: 24px; line-height: 1.6;">Double conversion online UPS systems providing uninterrupted, pure sine wave power with zero transfer time for critical data centers and life-saving equipment.</p>
            <div class="specs-grid" style="display: grid; gap: 16px;">
              <div style="display: flex; justify-content: space-between; padding-bottom: 16px; border-bottom: 1px solid var(--border-color);">
                <span style="color: var(--text-light); font-weight: 500;">Technology</span>
                <span style="color: var(--text-dark); font-weight: 600;">IGBT based Double Conversion</span>
              </div>
              <div style="display: flex; justify-content: space-between; padding-bottom: 16px; border-bottom: 1px solid var(--border-color);">
                <span style="color: var(--text-light); font-weight: 500;">Transfer Time</span>
                <span style="color: var(--text-dark); font-weight: 600;">0 milliseconds</span>
              </div>
              <div style="display: flex; justify-content: space-between; padding-bottom: 16px; border-bottom: 1px solid var(--border-color);">
                <span style="color: var(--text-light); font-weight: 500;">Power Factor</span>
                <span style="color: var(--text-dark); font-weight: 600;">Up to 0.99</span>
              </div>
            </div>
            <div style="margin-top: 32px;">
              <a href="contact.html" class="btn btn-primary">Request Quote</a>
            </div>
          </div>
        </div>

      </div>
    </section>
  </main>"""

update_file("about.html", about_main)
update_file("services.html", services_main)
update_file("sectors.html", sectors_main)
update_file("clients.html", clients_main)
update_file("contact.html", contact_main)
update_file("blog.html", blog_main)
update_file("products.html", products_main)

print("Pages fully populated.")
