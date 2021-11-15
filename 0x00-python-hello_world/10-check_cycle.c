#include "lists.h"

/**
 *check_cycle - checks if a singly linked list has a cycle in it
 *@list: The list to check
 *
 *Return: (0) if there is no cycle, (1) if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *doub = list;
	listint_t *reg = list;

	if (!list)
		return (0);

	while (doub && doub->next)
	{
		reg = reg->next;
		doub = doub->next->next;

		if (reg == doub)
			return (1);
	}
	return (0);
}
