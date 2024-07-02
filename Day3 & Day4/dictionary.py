#
# # DICTIONARY ARE MUTABLE
#
# info = {
#     "key" : "value",
#     "name": "Dev",
#     "Surename" : "Pavthawala",
#     "age": 21,
# "topics" : ("dict","set")
# }
#
# print(info)
# print(type(info))
# print(info["key"])
#
# info["name"] = "ved"
# print(info)
#
# info["Fname"] = "Tejash"
# print(info)


student={
    "name": "Dev",
    "surname" : "Pavthawala",
    "subject" : {
        "Maths" : 98,
        "English" :{
            "litrecture" :99,
            "Grammer" : 55
        },
        "hindi" : 100
    }

}


# nested dictionary
#
# print(student["subject"])
#
# print(f"for all keys : {student.keys()}")
# print(f"for all values : {student.values()}")
# print(f"for all items : {student.items()}")

print(student["name"]) # if key is wrong errors reflects
print(student.get("name")) # if key is worng errors not reflects it reflects NONE

# Update methord

student.update({"city" :"Surat"})
print(student)