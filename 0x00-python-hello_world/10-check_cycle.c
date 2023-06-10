#include "lists.h"

/**
 * check_cycle - checks if there is aa cycle in a linked list
 * @list: linked list
 * Return: 1 (True) 0 (False)
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *check;

	current = list;
	while (current != NULL)
	{
		check = current->next;
		while (check != NULL)
		{
			if (current == check)
				return (1);
			else
				check = check->next;
		}
		current = current->next;
	}
	return (0);
}
