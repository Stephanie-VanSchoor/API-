# =====================================================
#  API IMMOHUB - VERSION PYTHON (Flask)
#  Version gratuite pour démarrer
# =====================================================

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Permet à n'importe quel site d'utiliser l'API

# =====================================================
#  BASE DE DONNÉES SIMULÉE
#  (Tu remplaceras par des vraies données plus tard)
# =====================================================

estimates = {
    '75008': {
        'price': 1250000,
        'source': 'Base notariale 2025',
        'confidence': 98,
        'reference': 'DVF-2025-075-001284',
        'validator': 'Marie Dupont'
    },
    '75016': {
        'price': 890000,
        'source': 'DVF 2024',
        'confidence': 92,
        'reference': 'DVF-2024-075-089234',
        'validator': 'Luc Martin'
    },
    '75011': {
        'price': 620000,
        'source': 'Annonces (3 sources)',
        'confidence': 72,
        'reference': 'AGG-2025-011-004567',
        'validator': '— En cours'
    },
    '92100': {
        'price': 780000,
        'source': 'Cadastre + notaire',
        'confidence': 95,
        'reference': 'CAD-2025-092-000342',
        'validator': 'Sophie Lefèvre'
    },
    '75006': {
        'price': 420000,
        'source': 'Base notariale 2024',
        'confidence': 88,
        'reference': 'DVF-2024-075-076543',
        'validator': 'Révision nécessaire'
    },
    '75010': {
        'price': 2100000,
        'source': 'Base notariale 2025',
        'confidence': 97,
        'reference': 'DVF-2025-075-099123',
        'validator': 'Jean Moreau'
    }
}

# =====================================================
#  ROUTES DE L'API
# =====================================================

# Route d'accueil
@app.route('/')
def home():
    return jsonify({
        'name': 'ImmoHub API - Python',
        'version': '1.0.0',
        'status': '✅ En ligne',
        'endpoints': {
            'estimate': 'GET /estimate?postal=75008',
            'test': 'GET /test',
        }
    })

# Route de test
@app.route('/test')
def test():
    return jsonify({
        'message': '✅ L\'API fonctionne parfaitement !',
        'timestamp': datetime.now().isoformat(),
        'language': 'Python (Flask)'
    })

# Route principale : estimation
@app.route('/estimate')
def estimate():
    # Récupérer le code postal
    postal = request.args.get('postal')
    
    # Vérifier qu'un code postal est fourni
    if not postal:
        return jsonify({
            'error': '❌ Veuillez fournir un code postal. Exemple: /estimate?postal=75008',
            'usage': '/estimate?postal=75008'
        }), 400

    # Chercher le bien
    data = estimates.get(postal)
    
    if not data:
        return jsonify({
            'error': '❌ Aucune estimation trouvée pour ce code postal',
            'postal': postal,
            'available': list(estimates.keys())
        }), 404

    # Construire la réponse
    confidence_label = '🔥 Très fiable' if data['confidence'] >= 90 else \
                       '👍 Fiable' if data['confidence'] >= 70 else '⚠️ À vérifier'

    return jsonify({
        'success': True,
        'postal': postal,
        'estimate': data['price'],
        'formatted': f"{data['price']:,}".replace(',', ' ') + ' €',
        'source': data['source'],
        'confidence': data['confidence'],
        'confidence_label': confidence_label,
        'reference': data['reference'],
        'validated_by': data['validator'],
        'date': datetime.now().strftime('%Y-%m-%d'),
        'usage': {
            'plan': 'Starter (test)',
            'remaining_credits': 'Appels illimités pour le test'
        }
    })

# =====================================================
#  PAGE D'ABONNEMENT (interface simple)
# =====================================================

@app.route('/subscribe')
def subscribe():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>ImmoHub - Abonnement</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; }
            .plan { border: 2px solid #ddd; border-radius: 12px; padding: 20px; margin: 10px 0; }
            .plan:hover { border-color: #0070ba; background: #f5f9ff; }
            .plan h2 { margin: 0; color: #0b3b5c; }
            .plan .price { font-size: 28px; font-weight: bold; color: #0b3b5c; }
            .plan .period { color: #666; }
            .plan .features { color: #555; font-size: 14px; margin-top: 10px; }
            .btn { display: inline-block; background: #0070ba; color: white; padding: 12px 30px; border-radius: 8px; text-decoration: none; font-weight: bold; margin-top: 10px; }
            .btn:hover { background: #005ea6; }
            .btn-virement { background: #1a7a5a; }
            .btn-virement:hover { background: #1f8f6a; }
        </style>
    </head>
    <body>
        <h1>🏠 ImmoHub Pro</h1>
        <p>Choisissez votre formule d'abonnement :</p>

        <div class="plan">
            <h2>Starter</h2>
            <div><span class="price">49€</span> <span class="period">/mois</span></div>
            <div class="features">✅ 1 000 appels/mois<br>✅ Support email</div>
            <a href="#" class="btn btn-virement">📧 Payer par virement</a>
        </div>

        <div class="plan" style="border-color: #0070ba;">
            <h2>⭐ Pro</h2>
            <div><span class="price">199€</span> <span class="period">/mois</span></div>
            <div class="features">✅ 10 000 appels/mois<br>✅ Support prioritaire<br>✅ Données enrichies</div>
            <a href="#" class="btn btn-virement">📧 Payer par virement</a>
        </div>

        <div class="plan">
            <h2>Business</h2>
            <div><span class="price">799€</span> <span class="period">/mois</span></div>
            <div class="features">✅ Appels illimités<br>✅ Support dédié<br>✅ Données exclusives</div>
            <a href="#" class="btn btn-virement">📧 Payer par virement</a>
        </div>

        <p style="margin-top: 30px; font-size: 12px; color: #999;">
            💳 Paiement par virement bancaire (0% de frais)<br>
            📧 Contact : ton-email@gmail.com
        </p>
    </body>
    </html>
    """

# =====================================================
#  DÉMARRAGE DU SERVEUR
# =====================================================

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)