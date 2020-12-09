import time
import uuid
from typing import List
from uuid import UUID

from fastapi import HTTPException
from starlette import status

from app.app import app
from app.schemas import GetTaskSchema, CreateTaskSchema

TODO = []


@app.get('/todo', response_model=List[GetTaskSchema])
def get_tasks():
    return TODO


@app.post('/todo', status_code=status.HTTP_201_CREATED, response_model=GetTaskSchema)  # noqa: E501
def create_task(payload: CreateTaskSchema):
    task = payload.dict()
    task['id'] = uuid.uuid4()
    task['created'] = time.time()
    task['status'] = task['status'].value
    task['priority'] = task['priority'].value
    TODO.append(task)
    return task


@app.get('/todo/{task_id}', response_model=GetTaskSchema)
def get_task(task_id: UUID):
    for task in TODO:
        if task['id'] == task_id:
            return task
    raise HTTPException(
        status_code=404, detail=f'Task with ID {task_id} not found'
    )


@app.put('/todo/{task_id}', response_model=GetTaskSchema)
def update_task(task_id: UUID, payload: CreateTaskSchema):
    for task in TODO:
        if task['id'] == task_id:
            task.update(payload.dict())
            task['status'] = task['status'].value
            task['priority'] = task['priority'].value
            return task
    raise HTTPException(
        status_code=404, detail=f'Task with ID {task_id} not found'
    )


@app.delete('/todo/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: UUID):
    for index, task in enumerate(TODO):
        if task['id'] == task_id:
            TODO.pop(index)
            return
    raise HTTPException(
        status_code=404, detail=f'Order with ID {task_id} not found'
    )
