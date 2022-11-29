/**
 * insert_node - a fun.. in C that insert a number in linked list
 * @head: pointer for head of linked list
 * @number: valu to insert
 * Return: pointer of a new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	struct listint_t *ptr, *temp;

	if (head == NULL)
		return (NULL);
	ptr = *head;
	temp = (struct listint_t *)malloc(sizeof(struct listint_t));
	temp->n = number;
	temp->next = NULL;
	while (ptr->next != NULL)
	{
		ptr = ptr->next;
	}
	ptr->next = temp;
	return (temp);
}
