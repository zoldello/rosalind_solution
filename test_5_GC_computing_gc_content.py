import pytest
import problem_5_GC_computing_gc_content as sut


@pytest.mark.parametrize('fasta_records, expected', [
('''>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT''',
'''Rosalind_0808
60.91954'''),

('''>id1
AACCTTGG
>id2
AAGGCCCCCCGGGT''', 
'''id2
78.571429'''),

(None, None),

('', None),

(' ', None),
])
def test_get_highest_GC_Content_from_fasta(fasta_records, expected):
    target = sut.get_highest_GC_Content_from_fasta(fasta_records)
    assert target == expected


@pytest.mark.parametrize('fasta_records, exception',[
('''>id1
123AACCTTGG
>id2
AAGGCCCCCCGGGT''', 
ValueError),

('''>id1
AACCTTGG
>id2
AAGGCCCCCCGGGTxyz''', 
ValueError),
])
def test_get_highest_GC_Content_from_fasta_exceptions(fasta_records, exception):
    with pytest.raises(exception):
        target = sut.get_highest_GC_Content_from_fasta(fasta_records)

