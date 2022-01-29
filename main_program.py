import logging
from list_pkg.list_met import *
from tuple_pkg.tuple_met import *

logging.basicConfig(level=logging.DEBUG,filename="log_list_tup.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

try:
    logging.info("*********************************")
    logging.info("Starting with List")
    logging.info("*********************************")
    lst1 = [1,2,3,4,5,6,7,7,8,8,9,9,9,10]
    a_l = list_class(lst1)
    a_9 = a_l.list_count(9)
    a_8 = a_l.list_count(8)
    a_6 = a_l.list_count(6)
    logging.info("Count of element 9 :"+ str(a_9))
    logging.info("Count of element 8 :" + str(a_8))
    logging.info("Count of element 6 :" + str(a_6))
    sorted_lst = a_l.list_sort()
    logging.info("Sorted List :")
    logging.info(sorted_lst)
    logging.info("After popping element in index 1 :")
    logging.info(a_l.list_pop(1))
    logging.info("Inserting element 13 in position 2 :")
    logging.info(a_l.list_insert(2,13))
    logging.info("extending the list with [20,21,22]")
    logging.info(a_l.list_extend([20,21,22]))
    logging.info("Remove Element 10 from list")
    logging.info(a_l.list_remove(10))
    logging.info("Append Element 100 to list")
    logging.info(a_l.list_append(100))
    logging.info("Append list [12,13,14] to list")
    logging.info(a_l.list_append([12,13,14]))
    logging.info("*********************************")
    logging.info("Starting with Tuple")
    logging.info("*********************************")
    tup1 = (1,2,3,4,5,6,7,7,8,8,8,9)
    a_t = tuple_class(tup1)
    t_8 = a_t.tuple_count(8)
    t_9 = a_t.tuple_count(9)
    logging.info("Count of element 9 in tuple :"+ str(t_9))
    logging.info("Count of element 8 in tuple :"+ str(t_8))
    logging.info("Index of element 4 in tuple")
    logging.info(a_t.tuple_index(4))
    logging.info("Index of element 8 in tuple")
    logging.info(a_t.tuple_index(8))
    logging.info("Index of element 9 in tuple")
    logging.info(a_t.tuple_index(9))
    
except Exception as e:
    logging.exception(e)
        
