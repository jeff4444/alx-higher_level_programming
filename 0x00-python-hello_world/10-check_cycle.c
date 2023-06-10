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
	int i, j;

	i = 0;
	current = list;
	while (current != NULL)
	{
		check = list;
		j = 0;
		while (j != i)
		{
			if (current == check)
				return (1);
			else
				check = check->next;
			j++;
		}
		current = current->next;
		i++;
	}
	return (0);
}
