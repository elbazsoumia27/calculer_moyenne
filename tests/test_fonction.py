import sys
import os

# Add the parent directory to the path to import Fonction
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Fonction import calculer_moyenne, decision


class TestCalculerMoyenne:
    """Test cases for calculer_moyenne function"""
    
    def test_calculer_moyenne_basic(self):
        """Test basic average calculation"""
        result = calculer_moyenne(10, 12, 14)
        assert result == 12.0
    
    def test_calculer_moyenne_equal_values(self):
        """Test average with equal values"""
        result = calculer_moyenne(15, 15, 15)
        assert result == 15.0
    
    def test_calculer_moyenne_decimal(self):
        """Test average with decimal result"""
        result = calculer_moyenne(10, 11, 12)
        assert result == 11.0


class TestDecision:
    """Test cases for decision function"""
    
    def test_decision_admis_above_threshold(self):
        """Test decision returns 'Admis' when average > 10"""
        result = decision(15)
        assert result == "Admis"
    
    def test_decision_ajourn_below_threshold(self):
        """Test decision returns 'Ajourné' when average <= 10"""
        result = decision(8)
        assert result == "Ajourné"
    
    def test_decision_at_threshold(self):
        """Test decision at exact threshold (10)"""
        result = decision(10)
        assert result == "Ajourné"
    
    def test_decision_just_above_threshold(self):
        """Test decision just above threshold"""
        result = decision(10.1)
        assert result == "Admis"
