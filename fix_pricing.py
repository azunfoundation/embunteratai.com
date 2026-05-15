
import re

css = """
/* ══════════════════════════════════════════════
   PRICING PAGE STYLES
══════════════════════════════════════════════ */
.pr-included-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}
.pr-inc-item {
  background: var(--cream);
  padding: 24px;
  border-radius: var(--r-md);
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 12px;
  transition: var(--ease);
}
.pr-inc-item:hover {
  transform: translateY(-4px);
  background: var(--white);
  box-shadow: var(--shadow-sm);
}
.pr-inc-item span {
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--brown-dark);
}

.pr-cards {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}
.pr-card {
  background: var(--white);
  border-radius: var(--r-xl);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
  border: 1px solid var(--border);
  transition: var(--ease);
  position: relative;
}
.pr-card:hover {
  transform: translateY(-8px);
  box-shadow: var(--shadow-lg);
}
.pr-card-featured {
  border: 2px solid var(--gold);
  transform: scale(1.02);
  box-shadow: var(--shadow-md);
  z-index: 1;
}
.pr-card-featured:hover {
  transform: scale(1.02) translateY(-8px);
}
.pr-featured-badge {
  background: var(--gold);
  color: var(--white);
  text-align: center;
  padding: 8px 0;
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}
.pr-card-img {
  height: 200px;
  overflow: hidden;
}
.pr-card-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s ease;
}
.pr-card:hover .pr-card-img img { transform: scale(1.06); }
.pr-card-body {
  padding: 32px;
  display: flex;
  flex-direction: column;
  flex: 1;
}
.pr-card-head {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 16px;
  border-bottom: 1px solid var(--border);
  padding-bottom: 16px;
}
.pr-duration {
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--gold);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 4px;
}
.pr-card-head h3 {
  font-family: var(--font-h);
  font-size: 1.6rem;
  color: var(--brown-dark);
  margin: 0;
}
.pr-price-block {
  text-align: right;
}
.pr-price {
  font-family: var(--font-h);
  font-size: 1.8rem;
  font-weight: 700;
  color: var(--brown-dark);
  line-height: 1;
}
.pr-price-old {
  font-size: 0.9rem;
  text-decoration: line-through;
  color: var(--text-light);
  margin-top: 4px;
}
.pr-save {
  display: inline-block;
  background: rgba(160,123,74,0.1);
  color: var(--gold);
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 600;
  margin-top: 6px;
}
.pr-desc {
  font-size: 0.9rem;
  color: var(--text-light);
  line-height: 1.6;
  margin-bottom: 24px;
}
.pr-features {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 24px;
}
.pr-feat {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font-size: 0.9rem;
  color: var(--brown-dark);
}
.pr-feat svg {
  width: 18px;
  height: 18px;
  stroke: var(--gold);
  fill: none;
  stroke-width: 2;
  flex-shrink: 0;
  margin-top: 2px;
}
.pr-addon-box {
  background: var(--cream);
  border: 1px solid var(--border);
  border-radius: var(--r-sm);
  padding: 16px;
  margin-bottom: 32px;
  margin-top: auto;
}
.pr-addon-title {
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.05em;
  color: var(--gold-dark);
  margin-bottom: 12px;
}
.pr-addon-items {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}
.pr-addon-items span {
  background: var(--white);
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 0.8rem;
  color: var(--brown-dark);
  border: 1px solid var(--border);
}
.pr-card-actions {
  display: flex;
  gap: 12px;
}
.pr-btn-full {
  flex: 1;
  text-align: center;
  justify-content: center;
}

/* ─── Photo Strip ─── */
.pr-photo-strip {
  display: flex;
  height: 240px;
  overflow: hidden;
}
.pr-photo-strip img {
  width: 20%;
  height: 100%;
  object-fit: cover;
  transition: width 0.4s ease;
}
.pr-photo-strip img:hover {
  width: 25%;
}

/* ─── Modals ─── */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(5,4,2,0.8);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  opacity: 0;
  visibility: hidden;
  transition: var(--ease);
}
.modal-overlay.active {
  opacity: 1;
  visibility: visible;
}
.modal-content {
  background: var(--white);
  border-radius: var(--r-xl);
  width: 100%;
  max-width: 700px;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
  transform: translateY(20px);
  transition: var(--ease);
}
.modal-overlay.active .modal-content {
  transform: translateY(0);
}
.modal-close {
  position: absolute;
  top: 24px;
  right: 24px;
  background: var(--cream);
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  font-size: 1.2rem;
  color: var(--brown-dark);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: var(--ease);
  z-index: 10;
}
.modal-close:hover {
  background: var(--gold);
  color: #fff;
}
.modal-header {
  padding: 40px 40px 24px;
  border-bottom: 1px solid var(--border);
}
.modal-header h2 {
  font-family: var(--font-h);
  font-size: 2rem;
  color: var(--brown-dark);
  margin-bottom: 8px;
}
.modal-body {
  padding: 32px 40px 40px;
}
.modal-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
}
.modal-col h4 {
  font-size: 1.1rem;
  color: var(--gold-dark);
  margin-bottom: 16px;
  border-bottom: 1px solid var(--border);
  padding-bottom: 8px;
}
.modal-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.modal-list li {
  font-size: 0.9rem;
  color: var(--text-light);
  padding-left: 20px;
  position: relative;
}
.modal-list li::before {
  content: "•";
  position: absolute;
  left: 0;
  color: var(--gold);
}

/* ─── FAQ ─── */
.pr-faq-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr;
  gap: 48px;
}
.faq-container {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.faq-item {
  border: 1px solid var(--border);
  border-radius: var(--r-md);
  background: var(--white);
  overflow: hidden;
}
.faq-question {
  width: 100%;
  text-align: left;
  padding: 20px 24px;
  background: transparent;
  border: none;
  font-family: var(--font-b);
  font-size: 1.05rem;
  font-weight: 600;
  color: var(--brown-dark);
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.faq-icon {
  font-size: 1.5rem;
  font-weight: 300;
  color: var(--gold);
  transition: transform 0.3s ease;
}
.faq-question.active .faq-icon {
  transform: rotate(45deg);
}
.faq-answer {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.4s ease;
}
.faq-answer p {
  padding: 0 24px 24px;
  margin: 0;
  font-size: 0.95rem;
  color: var(--text-light);
  line-height: 1.6;
}
.pr-contact-card {
  background: var(--brown-dark);
  padding: 32px;
  border-radius: var(--r-lg);
  color: #fff;
  text-align: center;
}
.pr-contact-card h4 {
  font-family: var(--font-h);
  font-size: 1.4rem;
  margin-bottom: 12px;
}
.pr-contact-card p {
  font-size: 0.9rem;
  color: rgba(255,255,255,0.8);
  margin-bottom: 24px;
}

@media (max-width: 1024px) {
  .pr-cards { grid-template-columns: 1fr; }
  .pr-included-grid { grid-template-columns: repeat(2, 1fr); }
  .pr-faq-grid { grid-template-columns: 1fr; }
}
@media (max-width: 600px) {
  .pr-card-head { flex-direction: column; gap: 12px; }
  .pr-price-block { text-align: left; }
  .pr-card-actions { flex-direction: column; }
  .modal-grid { grid-template-columns: 1fr; }
  .pr-photo-strip { height: 160px; }
  .pr-included-grid { grid-template-columns: 1fr; }
}
"""

with open(r'c:\embunteratai.com\assets\css\style.css', 'a', encoding='utf-8') as f:
    f.write(css)

# NOW WRITE MODALS TO HTML
with open(r'c:\embunteratai.com\pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

modals_html = """
  <!-- MODALS -->
  <div id="modal-ayu" class="modal-overlay">
    <div class="modal-content">
      <button class="modal-close" onclick="closeModal('modal-ayu')">✕</button>
      <div class="modal-header">
        <p class="pr-duration">4 Days · 3 Nights</p>
        <h2>Ayu Rejuvenation</h2>
        <div class="pr-price" style="font-size:1.5rem;">RM 3,599</div>
      </div>
      <div class="modal-body">
        <div class="modal-grid">
          <div class="modal-col">
            <h4>Mother's Care</h4>
            <ul class="modal-list">
              <li>Premium room stay</li>
              <li>5x balanced meals daily</li>
              <li>1x Wellness Doctor Check</li>
              <li>Daily housekeeping</li>
              <li>Free flow herbal tea</li>
            </ul>
          </div>
          <div class="modal-col">
            <h4>Baby's Care</h4>
            <ul class="modal-list">
              <li>24/7 nursery support</li>
              <li>Jaundice monitoring</li>
              <li>Baby weight tracking</li>
              <li>Free baby clothes usage</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div id="modal-suri" class="modal-overlay">
    <div class="modal-content">
      <button class="modal-close" onclick="closeModal('modal-suri')">✕</button>
      <div class="modal-header">
        <p class="pr-duration">7 Days · 6 Nights</p>
        <h2>Suri Package</h2>
        <div class="pr-price" style="font-size:1.5rem;">RM 7,249</div>
      </div>
      <div class="modal-body">
        <div class="modal-grid">
          <div class="modal-col">
            <h4>Mother's Care</h4>
            <ul class="modal-list">
              <li>Premium room stay</li>
              <li>6x balanced meals daily</li>
              <li>1x Wellness Doctor Check</li>
              <li>3x Urut Berpantang (Massage)</li>
              <li>Param, Pilis &amp; Tapel</li>
              <li>Bertungku &amp; Tuam</li>
            </ul>
          </div>
          <div class="modal-col">
            <h4>Baby's Care</h4>
            <ul class="modal-list">
              <li>24/7 nursery support</li>
              <li>1x Paediatrician review</li>
              <li>Jaundice monitoring</li>
              <li>Free Nappico diapers</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div id="modal-anggun" class="modal-overlay">
    <div class="modal-content">
      <button class="modal-close" onclick="closeModal('modal-anggun')">✕</button>
      <div class="modal-header">
        <p class="pr-duration">14 Days · 13 Nights</p>
        <h2>Anggun Package</h2>
        <div class="pr-price" style="font-size:1.5rem;">RM 13,999</div>
      </div>
      <div class="modal-body">
        <div class="modal-grid">
          <div class="modal-col">
            <h4>Mother's Care</h4>
            <ul class="modal-list">
              <li>Premium room stay</li>
              <li>6x balanced meals daily</li>
              <li>2x Wellness Doctor Check</li>
              <li>5x Urut Berpantang (Massage)</li>
              <li>Full herbal therapies (Param, Pilis, Tapel, Bertungku, Bengkung)</li>
              <li>Lactation consultation</li>
            </ul>
          </div>
          <div class="modal-col">
            <h4>Baby's Care</h4>
            <ul class="modal-list">
              <li>24/7 nursery support</li>
              <li>2x Paediatrician review</li>
              <li>Jaundice monitoring</li>
              <li>Free Nappico diapers &amp; formula (if needed)</li>
              <li>Baby massage demonstration</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div id="modal-teratai" class="modal-overlay">
    <div class="modal-content">
      <button class="modal-close" onclick="closeModal('modal-teratai')">✕</button>
      <div class="modal-header">
        <p class="pr-duration">28 Days · 27 Nights</p>
        <h2>Teratai Package</h2>
        <div class="pr-price" style="font-size:1.5rem;">RM 25,999</div>
      </div>
      <div class="modal-body">
        <div class="modal-grid">
          <div class="modal-col">
            <h4>Mother's Care</h4>
            <ul class="modal-list">
              <li>Premium room stay</li>
              <li>6x balanced meals daily</li>
              <li>4x Wellness Doctor Check</li>
              <li>10x Urut Berpantang (Massage)</li>
              <li>1x Hair Wash Service</li>
              <li>3x Hot Blanket Therapy</li>
              <li>Full herbal therapies for 28 days</li>
            </ul>
          </div>
          <div class="modal-col">
            <h4>Baby's Care</h4>
            <ul class="modal-list">
              <li>24/7 nursery support</li>
              <li>4x Paediatrician review</li>
              <li>Free Nappico diapers &amp; wipes</li>
              <li>Comprehensive parentcraft training</li>
              <li>Professional newborn photoshoot</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
"""

# Insert modals before the <script> tag at the end of body
if '<script>' in html:
    html = html.replace('<script>', modals_html + '\n  <script>')
    with open(r'c:\embunteratai.com\pricing.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Modals added to HTML')
else:
    print('Could not find <script> tag to insert modals')

