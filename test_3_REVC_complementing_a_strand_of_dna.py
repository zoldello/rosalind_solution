import pytest
import problem_3_REVC_complementing_a_strand_of_dna as sut

@pytest.mark.parametrize('dna_string, expected',
[('AAAACCCGGT', 'ACCGGGTTTT'),
('A', 'T'),
('U', None),
('a', None),
('ACTG', 'CAGT'),
('', None),
(None, None),
('WACTG', None)])
def test_dna_string_reverse_complement(dna_string, expected):
    target = sut.dna_string_reverse_complement(dna_string)
    assert target == expected