"""
Views of the application

* CRUD ::
    Create
    Read
    Update
    Delete

* List ::

"""

from datetime import datetime
from typing import final

from .database.database import Database, tableTypes

from .database.models.people import Customer, Seller
from .database.models.product import Product


# Instance of temporary database object
appDatabase = Database()


def createRecord(recordType: tableTypes) -> bool:
    """ Function to handle addition of records to the table """
    try:
        if recordType == tableTypes.CUSTOMER or recordType == tableTypes.SELLER:
            print("#" + "-" * 79)
            print("Adding %s" % ("customer" if recordType == tableTypes.CUSTOMER else "seller"))
            print("#" + "-" * 79)

            # Get the entry values from the user
            personName    = str(input("Name: ") or "Joao")
            personSurname = str(input("Surname: ") or "da Silva")
            personAddress = str(input("Address: ") or "R dos Andradas 1011")
            personPhone   = int(input("Phone number: ") or "0119992993")
            print("Birth date:")
            personBirth   = datetime(int(input("\tyear:") or "2021"), int(input("\tmonth:") or "1"), int(input("\tday:") or "1"))

            # Object instance
            objPerson = None    # using reference to base of Customer and Seller (Person)

            # Update obbject instance according to user's choice
            if recordType == tableTypes.CUSTOMER:
                objPerson = Customer(personName, personSurname, personAddress, personPhone, personBirth, datetime.today())
            elif recordType == tableTypes.SELLER:
                objPerson = Seller(personName, personSurname, personAddress, personPhone, personBirth, datetime.today())

            # Adding to the database
            appDatabase.add(objPerson)
        elif recordType == tableTypes.PRODUCT:
            print("#" + "-" * 79)
            print("Adding product")
            print("#" + "-" * 79)

            # Get the entry values from the user
            prodDesc    = str(input("Product: ") or "Soccer ball")
            prodManuf   = str(input("Manufacturer: ") or "Penalty")
            prodPrice   = float(input("Price: ") or "10.0")

            # Object instance
            objProduct = Product(prodDesc, prodManuf, prodPrice)

            # Adding to the database
            appDatabase.add(objProduct)
        elif recordType == tableTypes.SALE:
            pass    # TO BE DONE
        else:
            raise Exception("Error!")

        return True
    except:
        return False


def readRecord(recordType: tableTypes) -> bool:
    """ Function to read records of the table """
    try:
        if recordType == tableTypes.CUSTOMER:
            print("reading customer")
        elif recordType == tableTypes.SELLER:
            print("reading seller")
        elif recordType == tableTypes.PRODUCT:
            print("reading product")
        elif recordType == tableTypes.SALE:
            print("reading sale")
        else:
            raise Exception("Error!")

        return True
    except:
        return False


def updateRecord(recordType: tableTypes) -> bool:
    """ Function to update records of the table """
    try:
        if recordType == tableTypes.CUSTOMER:
            print("updating customer")
        elif recordType == tableTypes.SELLER:
            print("updating seller")
        elif recordType == tableTypes.PRODUCT:
            print("updating product")
        elif recordType == tableTypes.SALE:
            print("updating sale")
        else:
            raise Exception("Error!")

        return True
    except:
        return False


def deleteRecord(recordType: tableTypes) -> bool:
    """ Function to delete records from the table """

    try:
        hdrType: str
        if recordType == tableTypes.CUSTOMER:
            hdrType = "customer"
        elif recordType == tableTypes.SELLER:
            hdrType = "seller"
        elif recordType == tableTypes.PRODUCT:
            hdrType = "product"
        elif recordType == tableTypes.SALE:
            hdrType = "sale"
        else:
            raise Exception("Error!")

        # Header to show user what is going on
        print("#" + "-" * 79)
        print(f"Deleting a {hdrType}")
        print("#" + "-" * 79)

        # Fist, show current records
        appDatabase.list(recordType)

        # Then ask the operator which ID to remove
        idToRemove = int(input("Which ID to delete: ") or "-1")

        # Try to remove (what could return error if ID does not exist)
        if appDatabase.remove(recordType, idToRemove):
            return True
        else:
            return False
    except:
        return False


def listAllRecords(recordType: tableTypes) -> bool:
    """ Function to list all records in the table """
    try:
        return appDatabase.list(recordType)
    except:
        return False
