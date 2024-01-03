#!/usr/bin/node
// script that computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const completedTasksCount = {};

    todos.forEach(todo => {
      const userId = todo.userId;
      const completed = todo.completed;

      if (completed) {
        completedTasksCount[userId] = (completedTasksCount[userId] || 0) + 1;
      }
    });
    console.log(completedTasksCount);
  }
});
