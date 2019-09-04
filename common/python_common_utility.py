########################################################
# script name: python_common_utility.py                #
# script details: This script will provide common      #
#                 functionality at one place           #
# created_by: Mr. Amol Shinde                          #
# modified by:                                         #
########################################################

import os
import mysql.connector
from mysql.connector import Error

class CommonUtils:
    def __init__(self):
        """
        This class is having all common methods.

        """

    def readFileContent(self,input_file_path):
        """
        This method is used to read file content.
        :param input_file_path: Take input file path as argument.
        :return: file content
        """
        try:

            file_content = ""
            # validate file path
            if os.path.isfile(input_file_path):
                log_message = 'Given input file path : ' + str(input_file_path) + ' contains file.'
                with open(input_file_path,'rb') as file:
                    file_content = file.read()
                return True, log_message, file_content
            else:
                log_message = 'Given input file path : ' + str(input_file_path) + ' is not correct, Please check...'
                return False, log_message, ''

        except Exception as e:
            log_message = 'Failed inside read_file_content() method. With ERROR : ' + str(e)
            return False, log_message, ''

    def decryptContent(self,file_content='',input_file_path=''):
        """
        This method is used to decrypt file_content.
        :param file_content: provide file content
        :param input_file_path: provide input file path
        :return: decrypted_file_content
        """
        try:
            decrypt_file_content=''

            # check given parameter for input file path
            if input_file_path:
                # create class object
                commonobj = CommonUtils()
                # get file content from input file path
                status, log_message, file_content = commonobj.readFileContent(
                                                        input_file_path=input_file_path)

                # validating above method execution
                if status:
                    # decrypt file content
                    decrypt_file_content = file_content.decode('base64', 'strict')
                    log_message = 'Successfully decrypted file content...'
                    return True, log_message, decrypt_file_content
                else:
                    return False, log_message, ''

        except Exception as e:
            log_message = 'Failed inside decrypt_content() method. Failed with ERROR : ' + str(e)
            return False, log_message, ''

    def mysqlConnect(self,host, database, user, password):
        """
        This method is used to create mysql connect object
        :param host: mysql host name
        :param database: mysql database name
        :param user: mysql user name
        :param password: mysql password
        :return: status, log_message, mysql connection object
        """
        try:
            print('mysql.connector.connect(host=' + str(host) + ',database=' + str(database) + ' ,user=' + str(
                user) + ',password= ' + str(password) + ')')
            connection = mysql.connector.connect(host=str(host),
                                                 database=str(database),
                                                 user=str(user),
                                                 password=str(password))


            log_message = 'Successfully generated connection object...'
            return True, log_message, connection
        except Exception as e:
            log_message = 'Failed inside mysql_connect(). Failed with ERROR : ' + str(e)
            return False, log_message, ''

    def retriveTableSchema(self,source_database_name,source_table_name,mysql_connect_obj):
        """
        This method will retrieve mysql table schema
        :param source_database_name: source database name.
        :param source_table_name: source table name
        :param mysql_connect_obj: mysql connection object
        :return: table schema [column name , datatype]
        """
        try:
            # create mysql cursor
            mysqlcursor = mysql_connect_obj.cursor()

            # mysql query

            mysqlcursor.execute("SELECT COLUMN_NAME,DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='genderstat_country';")

            mysqlresult = mysqlcursor.fetchall()
            log_message = 'Successfully fatched result...'
            return True, log_message, mysqlresult
        except Exception as e:
            log_message = 'Failed while running retriveTableSchema() method. Failed With ERROR : ' + str(e)
            return False, log_message, ''