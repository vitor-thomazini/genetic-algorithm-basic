import psycopg2;

from adapter import ExportReportPDF, ProductRepository
from domain import GeneticAlgorithm

if __name__ == "__main__":
    connection = psycopg2.connect(
        host="db", 
        port="5432", 
        user="postgres", 
        password="password", 
        database="mydb"
    )
    product_repository = ProductRepository(connection=connection)
    names, spaces, values  = product_repository.values()
    connection.close()

    runner = GeneticAlgorithm(population_size=len(names))
    chromosome = runner.run(mutation_probability=0.01, number_of_generations=10000, spaces=spaces, values=values, space_limit=3)

    total = 0
    for i in range(len(spaces)):
        if chromosome[i] == '1':
            total += values[i]
            print('Nome: %s R$ %s' % (names[i], values[i]))

    print("Melhor solução %s" % total)
    ExportReportPDF().export(runner.solutions)