import crud
from models import Project

# 新增数据
create_data = {
    "key": "abc",
    "name": "ABC"
}
result = crud.save(Project, create_data)
print(result)
# 查询所有数据
query_result = crud.query(Project)
print(query_result)
# 根据条件查询数据
query_result = crud.query(Project)
print(query_result)
query_result = crud.query(Project, Project.name == "ABC")
print(query_result)
query_result = crud.query(Project, Project.key == "abc", Project.name == "ABC")
print(query_result)
# 根据主键查询数据
query_result = crud.query_by_id(Project, 14236)
print(query_result.id, query_result.key, query_result.name, query_result.is_active, query_result.grab_status)
# 修改数据
update_data = {
    "grab_status": "成功",
    "key": "aaa"
}
result = crud.save(Project, update_data, query_result)
print(result.id, result.key, result.name, result.is_active, result.grab_status)
# 删除数据
crud.delete(Project, Project.key == "aaa")
