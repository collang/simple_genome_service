from service.repository import SequenceRepository


def handle_get_sequences(
    genome_repository: SequenceRepository        
):
    genome_repository.get