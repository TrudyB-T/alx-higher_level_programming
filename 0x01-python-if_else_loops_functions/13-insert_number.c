#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to the head of the node
 * @number: number to insert
 *
 * Return: the address of the new node, or NULL if it failed
 */


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *nunode;

	nunode = malloc(sizeof(listint_t));

	if (nunode == NULL)
	{
		return (NULL);
	}

	nunode->n = number;

	if (node == NULL || node->n >= number)
	{
		nunode->next = node;
		*head = nunode;
		return (nunode);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	nunode->next = node->next;
	node->next = nunode;

	return (nunode);
}
