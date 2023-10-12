import psycopg2;

from adapter import ExportReportPDF, ProductRepository
from domain import GenericAlgorithmDeap

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

    runner = GenericAlgorithmDeap(values=values, spaces=spaces, space_limit=9)
    result, info = runner.run(number_of_generations = 100, population_size = len(spaces))

    total = 0
    for i in range(len(spaces)):
        if result[i] == 1:
            total += values[i]
            print('Nome: %s R$ %s' % (names[i], values[i]))

    print("Melhor solução %s" % total)
    ExportReportPDF().export(info.select("max"))