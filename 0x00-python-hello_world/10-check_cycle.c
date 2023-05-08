#include "lists.h"
/**
 * check_cycle- function to checkif a singly linked list has a cycle in it.
 * @list: function parameter
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{

	listint_t *slow_ptr = list, *fast_ptr = list;

	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;

		if (slow_ptr == fast_ptr)
		{
			return (1);
		}
	}

	return (0);
}
