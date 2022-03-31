import pytest

from crawler import WIKI_PAGE_DEPTHS


class TestCrawler:
    def test_simple(self):
        page_depths = {
            "Sherutni_patrin": 0,
            "Romano_lekhipen": 1,
            "Sinti": 1,
            "Andalusiya": 2,
            "Indo-Europikane_chhiba": 2,
            "Kalo": 2,
            "Kontinento": 2,
            "Afrika": 3,
            "Eurasiya": 3,
            "Britanikane_dvipa": 3,
            "Sahel": 3,
            "Mêsire": 4,
            "China": 4,
            "Indekso_le_manushutne_baryaripnasko": 4,
            "New_York_City": 4,
            "Okeyanu": 4,
        }
        for p, d in page_depths.items():
            assert WIKI_PAGE_DEPTHS[p] == d
