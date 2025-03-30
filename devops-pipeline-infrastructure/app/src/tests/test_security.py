import subprocess
import requests

# URL de l'application Flask (modifiez si nécessaire)
BASE_URL = "http://localhost:8080"

def test_bandit_security_scan():
    """
    Exécute Bandit sur le code source et vérifie s'il y a des vulnérabilités.
    """
    print("🔍 Exécution de Bandit pour l'analyse de sécurité...")
    result = subprocess.run(["bandit", "-r", "../"], capture_output=True, text=True)
    
    print(result.stdout)  # Affiche le rapport Bandit dans la console
    
    assert "No issues identified." in result.stdout or "No issues found." in result.stdout, "⚠️ Bandit a détecté des vulnérabilités !"

def test_sql_injection_protection():
    """
    Vérifie si l'application est protégée contre une injection de SQL naïve.
    """
    print("🛡️ Vérification de la protection contre l'injection SQL...")

    payload = "' OR 1=1 --"
    response = requests.get(f"{BASE_URL}/multiply/{payload}/2")

    assert response.status_code == 400, "⚠️ L'application ne protège pas contre l'injection SQL !"
    
def test_sensitive_data_exposure():
    """
    Vérifie que l'application ne révèle pas d'informations sensibles dans ses réponses d'erreur.
    """
    print("🛑 Vérification des erreurs HTTP pour éviter l'exposition d'infos sensibles...")

    response = requests.get(f"{BASE_URL}/unknown_route")

    assert response.status_code == 404, "⚠️ L'application ne gère pas correctement les erreurs 404 !"
    assert "Traceback" not in response.text, "⚠️ L'application expose des détails internes dans les erreurs HTTP !"

if __name__ == "__main__":
    test_bandit_security_scan()
    test_sql_injection_protection()
    test_sensitive_data_exposure()

    print("✅ Tous les tests de sécurité sont passés avec succès ! 🎉")

