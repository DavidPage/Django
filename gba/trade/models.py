from django.db import models
from market.models import Market
from match.models import Match

class Trade(models.Model):
    match = models.ForeignKey(Match, related_name="match")
    market = models.ForeignKey(Market, related_name="market")
    invested = models.DecimalField(max_digits=5, decimal_places=2)
    profitLoss = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.invested

    def divide(self):
        return (int(self.profitLoss) * 100) / int(self.invested)
