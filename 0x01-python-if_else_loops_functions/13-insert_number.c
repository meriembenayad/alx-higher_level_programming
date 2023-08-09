#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head
 * @number: number to be added
 *
 * Return: pointer to new node || NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *tmp = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (0);
	new_node->n = number;

	if (tmp == NULL || tmp->n >= number)
	{
		new_node->next = tmp;
		*head = new_node;
		return (new_node);
	}

	while (tmp && tmp->next && tmp->next->n < number)
		tmp = tmp->next;

	new_node->next = tmp->next;
	tmp->next = new_node;

	return (new_node);
}
