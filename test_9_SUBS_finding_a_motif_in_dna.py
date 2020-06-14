import pytest
import problem_9_SUBS_finding_a_motif_in_dna as sut


@pytest.mark.parametrize('dna_substring, dna_string, expected',[
('ATAT', 'GATATATGCATATACTT', '2 4 10'),
('AC', 'ACTG', '1'),
('AC', None, None),
('ACTG', 'CCACTGA', '3'),
('G', 'XTG', None),
('X', 'ACTG', None),
('ACTGACTG', 'ACTG', None),
(None, 'ACTG', None),
('ACTG', '', None),
('', 'ACTG', None),
])
def test_get_substring_occurences(dna_substring, dna_string, expected):
    target = sut.get_substring_occurences(dna_substring, dna_string)
    assert target == expected
