#include "lists.h"

/**
 * reverse_listint -  reverses a listint_t linked list.
 * @head: pointer
 *
 * Return: a pointer to the first node of the reversed list
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	*head = prev;

	return (*head);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of linked list
 *
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	size_t s = 0;
	size_t j = 0;
	listint_t *t, *m, *r;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	t = *head;
	while (t != NULL)
	{
		s++;
		t = t->next;
	}

	t = *head;
	for (; j < (s / 2) - 1; j++)
	{
		t = t->next;
	}

	if ((s % 2) == 0 && t->n != t->next->n)
	{
		return (0);
	}

	t = t->next->next;
	r = reverse_listint(&t);
	m = r;

	t = *head;
	while (r != NULL)
	{
		if (t->n != r->n)
			return (0);
		t = t->next;
		r = r->next;
	}
	reverse_listint(&m);

	return (1);
}
