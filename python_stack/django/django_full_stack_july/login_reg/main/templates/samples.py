class TripManager(models.Manager):
    def trip_validator(self, postData):
        errors = {}
        if len(postData['destination']) == 0:
            errors['destination'] = "You must not leave this field empty!"
        if len(postData['destination']) < 3:
            errors['destination'] = "Destination must be longer than 3 characters"
        if len(postData['start_date']) == 0:
            errors['start_date'] = "Add a start date!"
        if len(postData['end_date']) == 0:
            errors['end_date'] = "Add an end date!"
        if len(postData['plan']) == 0:
            errors['plan'] = "What's your plan!?"
        if len(postData['plan']) < 2:
            errors['plan'] = "Really? That's all your going to do?!"

        return errors

    def edit_validator(sefl, postData)
        errors = {}
        if len(postData['update_destination']) == 0:
            errors['update_destination'] = "Please put something in this destination."
        if len(postData['update_destination']) < 3:
            errors['update_destination'] = "You destination needs more than 3 characters"

        if len(postData['update_plan']) == 0:
            errors['update_plan'] = "Please put something in your plan"
        if len(postData['update_plan']) < 3:
            errors['update_plan'] = "You plan needs more than 3 characters"

        if not postData['update_start_date']:
            errors['update_start_date'] = "Add an updated start date"
        if not postData['update_end_date']:
            errors['update_end_date'] = "Add an updated end date"

        return errors