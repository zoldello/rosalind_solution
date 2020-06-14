import pytest
import problem_2_RNA_transcribing_dna_into_rna as sut


@pytest.mark.parametrize('dna_string, expected',
[('AACCTTGG', 'AACCUUGG'),
('ACTG', 'ACUG'),
('GATGGAACTTGACTACGTAAATT', 'GAUGGAACUUGACUACGUAAAUU'),
('', None),
(None, None),
('WACTG', None)])
def test_transcribe_dna_to_rna(dna_string, expected):
    target = sut.transcribe_dna_to_rna(dna_string)
    assert target == expected
