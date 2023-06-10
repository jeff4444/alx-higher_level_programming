#include "lists.h"

/**
 * insert_node - inserts a number into a sorted linked list
 * @head: head of linked list
 * @number: number
 * Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *current;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	current = *head;
	newNode->n = number;
	newNode->next = NULL;
	if (current->n > number)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}
	while (current->next != NULL)
	{
		if (current->next->n > number)
		{
			temp = current->next;
			current->next = newNode;
			newNode->next = temp;
			return (newNode);
		}
		current = current->next;
	}
	current->next = newNode;
	return (newNode);
}
