
import re

with open(r'c:\embunteratai.com\services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract header (lines 1-56: everything up to and including mobile-nav-overlay div)
header_end = content.find('<div class="mobile-nav-overlay" id="mobileNavOverlay"></div>') + len('<div class="mobile-nav-overlay" id="mobileNavOverlay"></div>')

# Extract footer (from <footer onwards)
footer_start = content.find('<footer class="footer">')

header_part = content[:header_end]
footer_part = content[footer_start:]

new_body = '''

  <!-- ═══ HERO ═══ -->
  <section class="rm-hero">
    <div class="rm-hero-img">
      <img src="assets/images/herbs-images.jpg" alt="Traditional herbal therapy at Embun Teratai">
      <div class="rm-hero-overlay" style="background:linear-gradient(135deg,rgba(8,6,3,0.82) 0%,rgba(30,20,8,0.5) 55%,rgba(8,6,3,0.25) 100%);"></div>
    </div>
    <div class="rm-hero-content container">
      <span class="label" style="color:var(--gold-light);">Holistic Postnatal Therapies</span>
      <h1>Services &amp;<br><em>Therapies</em></h1>
      <p>Where ancient healing wisdom meets clinical-grade postpartum care — every therapy chosen to restore your body, mind, and spirit.</p>
      <div style="display:flex;gap:16px;flex-wrap:wrap;">
        <a href="booking.html" class="btn btn-primary">Book a Session</a>
        <a href="pricing.html" class="btn btn-outline" style="border-color:rgba(255,255,255,0.5);color:#fff;">View Packages</a>
      </div>
    </div>
  </section>

  <!-- ═══ INTRO ═══ -->
  <section class="section" style="padding-bottom:0;">
    <div class="container text-center">
      <span class="label">What We Offer</span>
      <h2 class="section-title">Comprehensive Care,<br>Head to Toe</h2>
      <p class="section-subtitle">Our service menu blends certified medical professionals, trained postnatal therapists, and time-honoured Malay healing traditions into one seamless recovery experience.</p>
    </div>
  </section>

  <!-- ═══ SERVICE PILLARS GRID ═══ -->
  <section class="section" style="padding-top:48px;">
    <div class="container">
      <div class="sv-pillars">

        <div class="sv-pillar">
          <div class="sv-pillar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/></svg>
          </div>
          <h4>Traditional Massage</h4>
          <p>Certified Malay postnatal massage for normal &amp; C-section delivery using premium herbal oils.</p>
        </div>

        <div class="sv-pillar">
          <div class="sv-pillar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/></svg>
          </div>
          <h4>Herbal Therapies</h4>
          <p>Bertungku, Tangas basah, Pilis, Tapel and the full suite of authentic postnatal herbal care.</p>
        </div>

        <div class="sv-pillar">
          <div class="sv-pillar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
          </div>
          <h4>Healing Cuisine</h4>
          <p>Award-winning chef-curated halal meals designed to nourish your body and boost milk production.</p>
        </div>

        <div class="sv-pillar">
          <div class="sv-pillar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>
          </div>
          <h4>Medical Care</h4>
          <p>24/7 nurse monitoring, in-house paediatrician consultations, and mother vital signs tracking.</p>
        </div>

        <div class="sv-pillar">
          <div class="sv-pillar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3z"/></svg>
          </div>
          <h4>Lactation Support</h4>
          <p>Personalized, pressure-free breastfeeding guidance from our certified lactation consultants.</p>
        </div>

        <div class="sv-pillar">
          <div class="sv-pillar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
          </div>
          <h4>Parentcraft</h4>
          <p>Expert-led workshops on newborn care, bonding, and bathing to build parental confidence.</p>
        </div>

      </div>
    </div>
  </section>

  <!-- ═══ FEATURE: TANAMERA OILS ═══ -->
  <section class="section section-alt" style="padding:80px 0;">
    <div class="container">
      <div class="rm-feature-row">
        <div class="rm-feature-img">
          <img src="assets/images/tanamera-herbal.webp" alt="Tanamera premium postnatal herbal oil">
        </div>
        <div class="rm-feature-text">
          <span class="label">Premium Partner</span>
          <h2>Tanamera<br>Herbal Excellence</h2>
          <p>We are proud to exclusively use <strong>Tanamera</strong> — Malaysia's most trusted premium herbal postnatal brand — for all our massage and therapy sessions. Tanamera oils are cold-pressed, 100% natural, and clinically formulated for postpartum recovery.</p>
          <ul class="rm-checklist">
            <li><span class="rm-check">✓</span> Postnatal massage for normal delivery</li>
            <li><span class="rm-check">✓</span> Postnatal massage for C-section delivery</li>
            <li><span class="rm-check">✓</span> Param, Pilis, Tapel &amp; Bengkung wrapping</li>
            <li><span class="rm-check">✓</span> Lulur (body scrub) &amp; full body care</li>
            <li><span class="rm-check">✓</span> 100% natural — safe for breastfeeding mothers</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- ═══ FEATURE: HERBAL THERAPIES ═══ -->
  <section class="section" style="padding:80px 0;">
    <div class="container">
      <div class="rm-feature-row reverse">
        <div class="rm-feature-img">
          <img src="assets/images/herbs-images.jpg" alt="Traditional herbal compress and spa therapy at Embun Teratai">
        </div>
        <div class="rm-feature-text">
          <span class="label">Authentic Healing</span>
          <h2>Bertungku &amp;<br>Herbal Therapies</h2>
          <p>Experience the deeply restorative practice of <strong>Bertungku</strong> (hot stone herbal compress) in our exclusive spa room. This time-honoured Malay therapy is essential for uterine recovery, breaking down fat deposits, and releasing trapped wind post-delivery.</p>
          <ul class="rm-checklist">
            <li><span class="rm-check">✓</span> Bertungku (tuam) &amp; Tangas basah steam therapy</li>
            <li><span class="rm-check">✓</span> Hot blanket &amp; full herbal bath immersion</li>
            <li><span class="rm-check">✓</span> Jamu herbal drinks for internal recovery</li>
            <li><span class="rm-check">✓</span> Relaxation spa therapies for mind &amp; body</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- ═══ THERAPY GALLERY ═══ -->
  <section class="section section-alt" style="padding:80px 0;">
    <div class="container">
      <div class="text-center" style="margin-bottom:56px;">
        <span class="label">Our Therapy Spaces</span>
        <h2 class="section-title">Where Healing Happens</h2>
        <p class="section-subtitle">Dedicated rooms designed for peace, privacy, and premium postnatal care.</p>
      </div>
      <div class="sv-therapy-gallery">
        <div class="sv-tg-item sv-tg-tall">
          <img src="assets/images/real-therapy-room.jpg" alt="Embun Teratai therapy room">
          <div class="sv-tg-label">Private Therapy Room</div>
        </div>
        <div class="sv-tg-item">
          <img src="assets/images/real-therapy-1.jpg" alt="Postnatal massage session">
          <div class="sv-tg-label">Postnatal Massage</div>
        </div>
        <div class="sv-tg-item">
          <img src="assets/images/real-therapy-2.jpg" alt="Herbal therapy at Embun Teratai">
          <div class="sv-tg-label">Herbal Therapy</div>
        </div>
        <div class="sv-tg-item">
          <img src="assets/images/real-therapy-products.jpg" alt="Postnatal therapy products">
          <div class="sv-tg-label">Premium Products</div>
        </div>
        <div class="sv-tg-item">
          <img src="assets/images/real-therapy-wide.jpg" alt="Wide view of therapy spa">
          <div class="sv-tg-label">Spa &amp; Wellness</div>
        </div>
      </div>
    </div>
  </section>

  <!-- ═══ FEATURE: HEALING CUISINE ═══ -->
  <section class="section" style="padding:80px 0;">
    <div class="container">
      <div class="rm-feature-row">
        <div class="sv-food-mosaic">
          <div class="sv-food-main">
            <img src="assets/images/real-food-spread.jpg" alt="Full postnatal meal spread at Embun Teratai">
          </div>
          <div class="sv-food-side">
            <img src="assets/images/real-food-salmon.jpg" alt="Salmon healing meal">
            <img src="assets/images/real-food-chicken.jpg" alt="Nourishing chicken dish">
          </div>
        </div>
        <div class="rm-feature-text">
          <span class="label">Chef-Curated Nutrition</span>
          <h2>Meals That<br>Heal &amp; Nourish</h2>
          <p>Our award-winning Executive Chef <strong>Marina Mustafa</strong> crafts every meal as part of your recovery. Each dish is halal-certified, nutrient-dense, and specifically designed to support postpartum healing and maximise milk production.</p>
          <ul class="rm-checklist">
            <li><span class="rm-check">✓</span> 3 nutritious halal-certified meals daily</li>
            <li><span class="rm-check">✓</span> Traditional confinement recipes &amp; Jamu drinks</li>
            <li><span class="rm-check">✓</span> Lactation-boosting superfoods &amp; herbs</li>
            <li><span class="rm-check">✓</span> Customized for dietary needs on request</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- ═══ FEATURE: LACTATION & MEDICAL ═══ -->
  <section class="section section-alt" style="padding:80px 0;">
    <div class="container">
      <div class="rm-feature-row reverse">
        <div class="rm-feature-img">
          <img src="images/Embun & Teratai/baby/AFS_0084.jpg" alt="Lactation and newborn care support at Embun Teratai">
        </div>
        <div class="rm-feature-text">
          <span class="label">24/7 Professional Support</span>
          <h2>Medical Care &amp;<br>Lactation Guidance</h2>
          <p>Rest easy knowing expert care is always just a call away. Our team of trained nurses, a certified lactation consultant, and an in-house paediatrician work around the clock to ensure both you and your baby are thriving.</p>
          <ul class="rm-checklist">
            <li><span class="rm-check">✓</span> 24/7 trained nurses &amp; caregivers on duty</li>
            <li><span class="rm-check">✓</span> Paediatrician-led newborn health monitoring</li>
            <li><span class="rm-check">✓</span> Certified lactation consultant support</li>
            <li><span class="rm-check">✓</span> Mother vital signs &amp; wound care monitoring</li>
            <li><span class="rm-check">✓</span> 24-hour CCTV for complete peace of mind</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- ═══ CTA ═══ -->
  <section class="cta-banner">
    <div class="container">
      <span class="label" style="color:var(--gold-light);">Begin Your Recovery</span>
      <h2>Ready to Experience<br>the Difference?</h2>
      <p>Book your stay today and let us take care of everything — so you can focus on what matters most.</p>
      <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;">
        <a href="booking.html" class="btn btn-white">Book Your Stay</a>
        <a href="pricing.html" class="btn btn-outline" style="border-color:rgba(255,255,255,0.4);color:#fff;">See Pricing</a>
      </div>
    </div>
  </section>

  '''

script_part = '''  <script>
    const header = document.getElementById('header');
    window.addEventListener('scroll', () => { header.classList.toggle('at-top', window.scrollY < 60); });
    document.getElementById('navToggle').addEventListener('click', () => { document.getElementById('navLinks').classList.toggle('active'); });
  </script>
</body>
</html>'''

new_content = header_part + new_body + footer_part.rstrip()

# Make sure script is at the end
if '<script>' not in new_content[new_content.rfind('</footer>'):]:
    new_content = new_content.rstrip() + '\n' + script_part

with open(r'c:\embunteratai.com\services.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Done!')
