import csv
from Station import Station
from Network import ColoredNetwork

def network_processer(file_path):
    nodes = []
    with open(file_path, 'r',  encoding='utf-8-sig') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in data:
            name = row[0]
            color = row[1]
            connections = [connection for connection in row[2:] if connection != '']
            node = Station(name, connections, color)
            nodes.append(node)
    return nodes

def get_start_end(nodes):
    start_name = input("Ingrese el nombre de la estación de inicio: ")
    end_name = input("Ingrese el nombre de la estación de fin: ")
    return start_name, end_name

def get_color():
    color = input("Ingrese el color del tren (Enter si no tiene color): ")
    return color