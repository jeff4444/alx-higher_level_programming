#include "lists.h"
/**
 * is_palindrome - checks if a linked lists is a palindrome
 * @head: head of list
 * Return: 1 (True) 0 (False)
 */
int is_palindrome(listint_t **head)
{
	int *list, i = 0, j, k;
	listint_t *current = *head;

	if (current == NULL)
		return (1);
	while (current != NULL)
	{
		i++;
		current = current->next;
	}
	if (i % 2 == 0)
	{
		list = malloc(sizeof(int) * (i / 2));
		j = i / 2;
	}
	else
	{
		list = malloc(sizeof(int) * ((i - 1) / 2));
		j = (i - 1) / 2;
	}
	current = *head;
	k = 0;
	while (k < j)
	{
		list[k] = current->n;
		current = current->next;
		k++;
	}
	if (i % 2)
		current = current->next;
	while (current != NULL)
	{
		if (list[k - 1] != current->n)
		{
			free(list);
			return (0);
		}
		current = current->next;
		k--;
	}
	free(list);
	return (1);
}

