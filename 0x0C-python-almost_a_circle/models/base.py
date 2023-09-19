#!/usr/bin/python3
"""class base"""
import json
import csv


class Base:
    """class named base"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"

        list_dictionaries = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(list_dictionaries)

        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            raise ValueError("Unsupported class type")

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**data) for data in dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            save to file csv
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".csv"

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == 'Rectangle':
                    data = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == 'Square':
                    data = [obj.id, obj.size, obj.x, obj.y]
                else:
                    raise ValueError("Unsupported class type")
                writer.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        """
            load from file csv
        """
        filename = cls.__name__ + ".csv"

        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == 'Rectangle':
                        data = {
                            'id': int(row[0]),
                            'width': int(row[1]),
                            'height': int(row[2]),
                            'x': int(row[3]),
                            'y': int(row[4])
                        }
                    elif cls.__name__ == 'Square':
                        data = {
                            'id': int(row[0]),
                            'size': int(row[1]),
                            'x': int(row[2]),
                            'y': int(row[3])
                        }
                    else:
                        raise ValueError("Unsupported class type")
                    instance = cls.create(**data)
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []
