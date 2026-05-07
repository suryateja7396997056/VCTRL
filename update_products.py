import re

with open("products.html", "r") as f:
    content = f.read()

additional_products = """
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: center; margin-bottom: 80px;" class="reveal">
          <div class="product-details" style="order: 2;">
            <h2 style="font-size: 2.5rem; margin-bottom: 16px; color: var(--text-dark);">Power Conditioners</h2>
            <p style="color: var(--text-light); margin-bottom: 24px; line-height: 1.6;">Our robust power conditioners integrate voltage regulation, isolation, and noise filtering into a single compact unit to give you complete peace of mind.</p>
            <div class="specs-grid" style="display: grid; gap: 16px;">
              <div style="display: flex; justify-content: space-between; padding-bottom: 16px; border-bottom: 1px solid var(--border-color);">
                <span style="color: var(--text-light); font-weight: 500;">Protection</span>
                <span style="color: var(--text-dark); font-weight: 600;">Spikes, Surges, Noise</span>
              </div>
              <div style="display: flex; justify-content: space-between; padding-bottom: 16px; border-bottom: 1px solid var(--border-color);">
                <span style="color: var(--text-light); font-weight: 500;">Voltage Regulation</span>
                <span style="color: var(--text-dark); font-weight: 600;">± 1% Precision</span>
              </div>
              <div style="display: flex; justify-content: space-between; padding-bottom: 16px; border-bottom: 1px solid var(--border-color);">
                <span style="color: var(--text-light); font-weight: 500;">Response Time</span>
                <span style="color: var(--text-dark); font-weight: 600;">Instantaneous</span>
              </div>
            </div>
            <div style="margin-top: 32px;">
              <a href="contact.html" class="btn btn-primary">Request Quote</a>
            </div>
          </div>
          <div class="product-media" style="height: auto; order: 1;">
            <img src="https://images.pexels.com/photos/236089/pexels-photo-236089.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Power Conditioner" style="width: 100%; border-radius: 12px; box-shadow: var(--shadow-lg);">
          </div>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: center; margin-bottom: 80px;" class="reveal">
          <div class="product-media" style="height: auto;">
            <img src="https://images.pexels.com/photos/110854/pexels-photo-110854.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Power Distribution Unit" style="width: 100%; border-radius: 12px; box-shadow: var(--shadow-lg);">
          </div>
          <div class="product-details">
            <h2 style="font-size: 2.5rem; margin-bottom: 16px; color: var(--text-dark);">Power Distribution Units (PDU)</h2>
            <p style="color: var(--text-light); margin-bottom: 24px; line-height: 1.6;">We are the only manufacturers in South India with the potential to design and manufacture custom Power Distribution Units of any capacity for Data Centers and IT Parks.</p>
            <div class="specs-grid" style="display: grid; gap: 16px;">
              <div style="display: flex; justify-content: space-between; padding-bottom: 16px; border-bottom: 1px solid var(--border-color);">
                <span style="color: var(--text-light); font-weight: 500;">Monitoring</span>
                <span style="color: var(--text-dark); font-weight: 600;">Intelligent Branch Circuit</span>
              </div>
              <div style="display: flex; justify-content: space-between; padding-bottom: 16px; border-bottom: 1px solid var(--border-color);">
                <span style="color: var(--text-light); font-weight: 500;">Customization</span>
                <span style="color: var(--text-dark); font-weight: 600;">Fully Scalable & Custom</span>
              </div>
              <div style="display: flex; justify-content: space-between; padding-bottom: 16px; border-bottom: 1px solid var(--border-color);">
                <span style="color: var(--text-light); font-weight: 500;">Safety Standards</span>
                <span style="color: var(--text-dark); font-weight: 600;">Global Compliance</span>
              </div>
            </div>
            <div style="margin-top: 32px;">
              <a href="contact.html" class="btn btn-primary">Request Quote</a>
            </div>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: center;" class="reveal">
          <div class="product-details" style="order: 2;">
            <h2 style="font-size: 2.5rem; margin-bottom: 16px; color: var(--text-dark);">Electrical Panels</h2>
            <p style="color: var(--text-light); margin-bottom: 24px; line-height: 1.6;">High-quality custom electrical control panels including LT/HT Panels, APFC Panels, and Motor Control Centers engineered for heavy industrial requirements.</p>
            <div class="specs-grid" style="display: grid; gap: 16px;">
              <div style="display: flex; justify-content: space-between; padding-bottom: 16px; border-bottom: 1px solid var(--border-color);">
                <span style="color: var(--text-light); font-weight: 500;">Enclosure</span>
                <span style="color: var(--text-dark); font-weight: 600;">IP54 / IP55 Rated</span>
              </div>
              <div style="display: flex; justify-content: space-between; padding-bottom: 16px; border-bottom: 1px solid var(--border-color);">
                <span style="color: var(--text-light); font-weight: 500;">Components</span>
                <span style="color: var(--text-dark); font-weight: 600;">Premium Switchgears</span>
              </div>
              <div style="display: flex; justify-content: space-between; padding-bottom: 16px; border-bottom: 1px solid var(--border-color);">
                <span style="color: var(--text-light); font-weight: 500;">Testing</span>
                <span style="color: var(--text-dark); font-weight: 600;">100% Factory Tested</span>
              </div>
            </div>
            <div style="margin-top: 32px;">
              <a href="contact.html" class="btn btn-primary">Request Quote</a>
            </div>
          </div>
          <div class="product-media" style="height: auto; order: 1;">
            <img src="https://images.pexels.com/photos/257736/pexels-photo-257736.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Electrical Panel" style="width: 100%; border-radius: 12px; box-shadow: var(--shadow-lg);">
          </div>
        </div>

      </div>
    </section>
  </main>"""

# Replace the closing of the section and main
content = content.replace("      </div>\n    </section>\n  </main>", additional_products)
with open("products.html", "w") as f:
    f.write(content)
