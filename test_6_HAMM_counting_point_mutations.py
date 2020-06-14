import pytest
import problem_6_HAMM_counting_point_mutations as sut



@pytest.mark.parametrize('dna_string_1, dna_string_2, expected',[
('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT', 7),
('ACTG', 'ACTG', 0),
('ACTG', 'CCTG', 1),
('ACTG', 'CG', None),
('', 'CTCTG', None),
('ACTC', None, None),
])
def test_get_hamming_distance(dna_string_1, dna_string_2, expected):
    target = sut.get_hamming_distance(dna_string_1, dna_string_2)
    assert target == expected
