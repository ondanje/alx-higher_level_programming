#include"lists.h"
/**
 * insert_node-inserts a number into a sorted singly linked list.
 * @head: function parameter
 * @number: function parameter
 * Return: list
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
		/*failed to allocate memory for new node*/
	}
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		/*insert at the beginning of the list*/
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		/*insert in the middle or at the end of the list*/
		listint_t *current = *head;

		while (current->next != NULL && current->next->n < number)
		{
			current = current->next;
		}
		new_node->next = current->next;
		current->next = new_node;
	}

	return (new_node);
}
