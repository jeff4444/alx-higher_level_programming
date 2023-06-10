#include "lists.h"

/**
 * check_cycle - checks if there is aa cycle in a linked list
 * @list: linked list
 * Return: 1 (True) 0 (False)
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list->next;

	while (current != NULL)
	{
		if (current == list)
			return (1);
		else
			current = current->next;
	}
	return (0);
}
