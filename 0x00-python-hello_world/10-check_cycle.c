#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to list
 * Return: O || 1
 */
int check_cycle(listint_t *list)
{
	listint_t *first_node, *second_node;

	first_node = list;
	if(list == NULL || list->next == NULL)
		return (0);

	first_node = list;
	second_node = list;

	while(first_node && second_node && second_node->next)
	{
		first_node = first_node->next;
		second_node = second_node->next->next;

		if(first_node == second_node)
			return (1);
	}

	return (0);
}
