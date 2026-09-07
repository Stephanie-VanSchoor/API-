// EXEMPLE D'APPEL API
// L'utilisateur envoie une adresse, l'API renvoie l'estimation

GET https://api.immohub.com/v1/estimate?address=12+rue+de+la+Paix+75008+Paris

// RÉPONSE DE L'API (format JSON)
{
  "success": true,
  "data": {
    "address": "12 rue de la Paix, 75008 Paris",
    "estimated_value": 1250000,
    "confidence": 98,
    "sources": [
      {
        "name": "Base notariale 2025",
        "date": "15/06/2025",
        "reference": "DVF-2025-075-001284"
      }
    ],
    "validated_by": "Marie Dupont"
  },
  "usage": {
    "remaining_credits": 9876,
    "plan": "Pro"
  }
}