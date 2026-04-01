import streamlit as st
import pandas as pd
from datetime import datetime

# Forcer le thème clair
st.config.set_option('theme.base', 'light')
st.config.set_option('theme.primaryColor', '#667eea')  # Vos couleurs
st.config.set_option('theme.backgroundColor', '#ffffff')
st.config.set_option('theme.secondaryBackgroundColor', '#f0f2f6')
st.config.set_option('theme.textColor', '#262730')
st.config.set_option('theme.font', 'sans serif')

# Configuration de la page
st.set_page_config(
    page_title="AskYourCSV - Assistant IA pour vos données",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personnalisé pour un design moderne
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hero Section */
    .hero {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 4rem 2rem;
        border-radius: 0 0 50px 50px;
        color: white;
        text-align: center;
        margin-bottom: 3rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .hero h1 {
        font-size: 4rem;
        font-weight: 800;
        margin-bottom: 1rem;
        animation: fadeInDown 1s ease;
    }
    
    .hero p {
        font-size: 1.3rem;
        opacity: 0.95;
        max-width: 800px;
        margin: 0 auto 2rem auto;
        animation: fadeInUp 1s ease 0.3s both;
    }
    
    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,0.2);
        padding: 0.5rem 1.5rem;
        border-radius: 50px;
        font-weight: 500;
        margin-bottom: 1.5rem;
        animation: fadeIn 1s ease;
    }
    
    /* Features Section */
    .section-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        color: #2d3748;
        margin-bottom: 3rem;
        position: relative;
    }
    
    .section-title:after {
        content: '';
        display: block;
        width: 80px;
        height: 4px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        margin: 1rem auto;
        border-radius: 2px;
    }
    
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        height: 100%;
        border: 1px solid #e2e8f0;
        text-align: center;
    }
    
    .feature-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 8px 30px rgba(102, 126, 234, 0.15);
        border-color: #667eea;
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .feature-card h3 {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 1rem;
    }
    
    .feature-card p {
        color: #718096;
        line-height: 1.6;
    }
    
    /* Stats Section */
    .stats-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 4rem 2rem;
        border-radius: 50px;
        margin: 4rem 0;
        color: white;
    }
    
    .stat-item {
        text-align: center;
        padding: 1rem;
    }
    
    .stat-number {
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 1.1rem;
        opacity: 0.9;
    }
    
    /* Use Cases */
    .usecase-card {
        background: #f7fafc;
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 1rem;
        border-left: 4px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .usecase-card:hover {
        background: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* Pricing Cards */
    .pricing-card {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        text-align: center;
        transition: all 0.3s ease;
        height: 100%;
        border: 2px solid transparent;
    }
    
    .pricing-card:hover {
        border-color: #667eea;
        transform: scale(1.02);
    }
    
    .pricing-card.popular {
        border-color: #667eea;
        box-shadow: 0 8px 30px rgba(102, 126, 234, 0.2);
        position: relative;
    }
    
    .popular-badge {
        position: absolute;
        top: -12px;
        left: 50%;
        transform: translateX(-50%);
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.25rem 1.5rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
    }
    
    .price {
        font-size: 2.5rem;
        font-weight: 700;
        color: #2d3748;
        margin: 1rem 0;
    }
    
    .price-period {
        font-size: 1rem;
        color: #718096;
    }
    
    .feature-list {
        list-style: none;
        padding: 0;
        margin: 2rem 0;
        text-align: left;
    }
    
    .feature-list li {
        padding: 0.5rem 0;
        color: #4a5568;
    }
    
    .feature-list li:before {
        content: "✓";
        color: #667eea;
        font-weight: bold;
        margin-right: 0.5rem;
    }
    
    .cta-button {
        display: inline-block;
        background: linear-gradient(135deg, #00b894 0%, #00cec9 100%);
        color: white;
        padding: 0.75rem 2rem;
        border-radius: 10px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
    }
    .cta-button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 15px rgba(0, 184, 148, 0.4);
    }
    
    .cta-button.secondary {
        background: white;
        color: #667eea;
        border: 2px solid #667eea;
    }
    
    .cta-button.secondary:hover {
        background: #667eea;
        color: white;
    }
    
    /* Footer */
    .footer {
        background: #1a202c;
        color: white;
        padding: 3rem 2rem;
        border-radius: 50px 50px 0 0;
        margin-top: 4rem;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <span class="hero-badge">🤖 L'IA au service de vos données</span>
    <h1>AskYourCSV</h1>
    <p>Transformez vos fichiers CSV en conversations intelligentes.<br>Posez des questions en langage naturel, obtenez des réponses instantanées.</p>
    <div style="display: flex; gap: 1rem; justify-content: center; margin-top: 2rem;">
        <a href="https://askyourcsv-playground-production.up.railway.app" target="_self" class="cta-button">🎯 Essayer le playground</a>
        <a href="https://t.me/askyourcsv_bot" target="_blank" class="cta-button secondary">📱 Découvrir le bot Telegram</a>
    </div>
    <p style="margin-top: 2rem; font-size: 0.9rem; opacity: 0.8;">
        ⚡ Aucune inscription • Votre clé API personnelle • 100% privé
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Features Section
st.markdown("<h2 class='section-title'>Pourquoi choisir AskYourCSV ?</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🔍</div>
        <h3>Analyse Intelligente</h3>
        <p>Posez des questions sur vos données. Notre IA comprend le contexte et fournit des réponses précises basées sur vos fichiers.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <h3>Multi-Plateforme</h3>
        <p>Accédez à vos données depuis notre playground web ou directement sur Telegram. Analysez où que vous soyez.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🛡️</div>
        <h3>100% Privé</h3>
        <p>Vos données restent confidentielles. Utilisez votre propre clé API, aucun stockage permanent de vos fichiers.</p>
    </div>
    """, unsafe_allow_html=True)


# Use Cases
st.markdown("<br/><h2 class='section-title'>Cas d'utilisation</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="usecase-card">
        <h4 style="color: #2d3748; margin-bottom: 0.5rem;">📊 Analyse Financière</h4>
        <p style="color: #718096;">Interrogez vos rapports financiers, trouvez les tendances, calculez des moyennes et identifiez les anomalies en quelques secondes.</p>
    </div>
    <div class="usecase-card">
        <h4 style="color: #2d3748; margin-bottom: 0.5rem;">🛍️ E-commerce</h4>
        <p style="color: #718096;">Analysez vos ventes, suivez les stocks, identifiez les produits les plus performants directement depuis votre catalogue.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="usecase-card">
        <h4 style="color: #2d3748; margin-bottom: 0.5rem;">🎓 Recherche Académique</h4>
        <p style="color: #718096;">Explorez vos données de recherche, croisez des variables, obtenez des insights sans écrire une seule ligne de code.</p>
    </div>
    <div class="usecase-card">
        <h4 style="color: #2d3748; margin-bottom: 0.5rem;">📈 Marketing</h4>
        <p style="color: #718096;">Analysez vos campagnes, segmentez vos clients, mesurez la performance de vos actions marketing en temps réel.</p>
    </div>
    """, unsafe_allow_html=True)

# How it works
st.markdown("<h2 class='section-title'>Comment ça marche ?</h2>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-card" style="padding: 1.5rem;">
        <div style="font-size: 2rem; font-weight: 700; color: #667eea;">1</div>
        <h4 style="margin: 0.5rem 0;">Upload</h4>
        <p style="font-size: 0.9rem;">Importez votre fichier CSV en un clic</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card" style="padding: 1.5rem;">
        <div style="font-size: 2rem; font-weight: 700; color: #667eea;">2</div>
        <h4 style="margin: 0.5rem 0;">Configurez</h4>
        <p style="font-size: 0.9rem;">Choisissez votre modèle IA et votre clé API</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card" style="padding: 1.5rem;">
        <div style="font-size: 2rem; font-weight: 700; color: #667eea;">3</div>
        <h4 style="margin: 0.5rem 0;">Posez</h4>
        <p style="font-size: 0.9rem;">Interrogez vos données en français</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card" style="padding: 1.5rem;">
        <div style="font-size: 2rem; font-weight: 700; color: #667eea;">4</div>
        <h4 style="margin: 0.5rem 0;">Obtenez</h4>
        <p style="font-size: 0.9rem;">Recevez des réponses précises instantanément</p>
    </div>
    """, unsafe_allow_html=True)

# FAQ Section
st.markdown("<h2 class='section-title'>Questions fréquentes</h2>", unsafe_allow_html=True)

faqs = [
    ("🔐 Mes données sont-elles sécurisées ?", "Oui ! Vos données ne sont jamais stockées sur nos serveurs. Dans le playground, vous utilisez votre propre clé API, garantissant une confidentialité totale."),
    ("🤖 Quels modèles d'IA puis-je utiliser ?", "AskYourCSV supporte Google Gemini et OpenAI GPT. Vous pouvez choisir le modèle qui correspond le mieux à vos besoins dans la configuration."),
    ("📱 Comment accéder au bot Telegram ?", "Recherchez @askyourcsv_bot sur Telegram et démarrez la conversation avec /start. C'est gratuit et instantané !"),
]

for question, answer in faqs:
    with st.expander(question):
        st.write(answer)

# CTA Final
st.markdown("""
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 4rem 2rem; border-radius: 50px; text-align: center; margin: 4rem 0;">
    <h2 style="color: white; font-size: 2.5rem; margin-bottom: 1rem;">Prêt à transformer vos données ?</h2>
    <p style="color: white; font-size: 1.2rem; opacity: 0.9; margin-bottom: 2rem;">Rejoignez des milliers d'utilisateurs qui analysent leurs CSV plus intelligemment</p>
    <div style="display: flex; gap: 1rem; justify-content: center;">
        <a href="https://askyourcsv-playground-production.up.railway.app" target="_self" class="cta-button" style="background: white; color: #667eea;">🎯 Essayer maintenant</a>
        <a href="https://t.me/askyourcsv_bot" target="_blank" class="cta-button" style="background: transparent; border: 2px solid white; color: white;">📱 Tester le bot</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; margin-bottom: 2rem;">
        <div>
            <h4 style="color: white; margin-bottom: 1rem;">AskYourCSV</h4>
            <p style="color: #a0aec0; font-size: 0.9rem;">L'IA qui parle à vos données</p>
        </div>
        <div>
            <h4 style="color: white; margin-bottom: 1rem;">Produit</h4>
            <ul style="list-style: none; padding: 0; color: #a0aec0;">
                <li style="margin-bottom: 0.5rem;"><a href="#" style="color: #a0aec0; text-decoration: none;">Fonctionnalités</a></li>
                <li style="margin-bottom: 0.5rem;"><a href="#" style="color: #a0aec0; text-decoration: none;">Tarifs</a></li>
                <li style="margin-bottom: 0.5rem;"><a href="#" style="color: #a0aec0; text-decoration: none;">FAQ</a></li>
            </ul>
        </div>
        <div>
            <h4 style="color: white; margin-bottom: 1rem;">Légal</h4>
            <ul style="list-style: none; padding: 0; color: #a0aec0;">
                <li style="margin-bottom: 0.5rem;"><a href="#" style="color: #a0aec0; text-decoration: none;">Confidentialité</a></li>
                <li style="margin-bottom: 0.5rem;"><a href="#" style="color: #a0aec0; text-decoration: none;">Conditions d'utilisation</a></li>
                <li style="margin-bottom: 0.5rem;"><a href="#" style="color: #a0aec0; text-decoration: none;">Mentions légales</a></li>
            </ul>
        </div>
        <div>
            <h4 style="color: white; margin-bottom: 1rem;">Contact</h4>
            <ul style="list-style: none; padding: 0; color: #a0aec0;">
                <li style="margin-bottom: 0.5rem;">dimension.adresse@gmail.com</li>
                <li style="margin-bottom: 0.5rem;">@ Dimension Technology</li>
            </ul>
        </div>
    </div>
    <div style="text-align: center; padding-top: 2rem; border-top: 1px solid #2d3748; color: #718096;">
        © 2026 AskYourCSV. Tous droits réservés. Développé avec ❤️
    </div>
</div>
""", unsafe_allow_html=True)