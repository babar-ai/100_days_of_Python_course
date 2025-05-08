import info

info.information("ali")
info.new_info("22mdbcs241")  #new define method

#note that some times if we define a new method in "info.py" file and then directly try to import that method here then it will generate an runtime error. it is bcz python not reload the file bydefault,
# to solve this problem we have to explicitly reload the import file( info.py in this case) by using 

from importlib import reload
reload(info)

marks = 555
print(id(marks))