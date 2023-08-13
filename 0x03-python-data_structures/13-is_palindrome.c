#include "lists.h"
#include <stdio.h>
/**
 * reverseList - return the head of reversed linked list
 * @head: pointer to head of a linked list
 *
 * Return: reversed head
 */
listint_t *reverseList(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return prev;
}
/**
 * is_palindrome - checks if the integer is palindrome
 * @head: pointer to head of a linked list
 *
 * Return: 0 NOT PLINDROME || 1 PALINDROME
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow, *sec_half;
	int palind = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	slow = *head;
	fast = *head;
	prev_slow = *head;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
		slow = slow->next;

	sec_half = reverseList(slow);
	slow = sec_half;

	while (sec_half != NULL)
	{
		if ((*head)->n != sec_half->n)
		{
			palind = 0;
			break;
		}
		*head = (*head)->next;
		sec_half = sec_half->next;
	}

	prev_slow->next = reverseList(slow);

	return (palind);
}
