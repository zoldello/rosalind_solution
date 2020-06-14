import pytest
import problem_8_PROT_translating_rna_into_protein as sut


@pytest.mark.parametrize('rna_string, expected',[
('UUUCUUAUU', 'FLI'),
('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA', 'MAMAPRTEINSTRING'),
('', None),
(None, None, ),
])
def test_translate_rna_to_protein(rna_string, expected):
    target = sut.translate_rna_to_protein(rna_string)
    assert target == expected


@pytest.mark.parametrize('rna_string, exception',[
    ('XYZ', ValueError),
])
def test_translate_rna_to_protein_exception_raising(rna_string, exception):
    with pytest.raises(exception):
        sut.translate_rna_to_protein(rna_string)
