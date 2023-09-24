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

    products = product_repository.values()

    connection.close()
    spaces = []
    values = []
    names = []
    for product in products:
        spaces.append(product.space)
        values.append(product.value)
        names.append(product.name)

    runner = GeneticAlgorithm(population_size=len(products))
    chromosome = runner.run(mutation_probability=0.01, number_of_generations=100000, spaces=spaces, values=values, space_limit=3)

    for i in range(len(products)):
        if chromosome[i] == '1':
            print('Nome: %s R$ %s' % (products[i].name, products[i].value))

    ExportReportPDF().export(runner.solutions)