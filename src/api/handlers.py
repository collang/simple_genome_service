from service.repository import GenomeRepository


def handle_get_sequences(
    genome_repository: GenomeRepository        
):
    genome_repository.get