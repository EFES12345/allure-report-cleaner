from datetime import datetime, timedelta

import typer

import work_with_data


def parse_value(value: str):
    if value.isnumeric():
        _value = datetime.now() - timedelta(days=int(value))
        return _value.date().isoformat()

    try:
        _value = datetime.strptime(value, '%Y-%m-%d')
        return _value.date().isoformat()
    except ValueError:
        raise typer.BadParameter('Переданное значение не является ни числом, ни датой в формате ISO (%Y-%m-%d)')


def main(
        value: str = typer.Argument(
            help='Дата, до которой будут удалены данные (включительно). '
                 'Можно передать количество дней относительно сегодняшней даты',
            parser=parse_value
        )
):
    work_with_data.delete_data(value)
    work_with_data.rebuild_report()
    print(f"Очищены все поля начиная с {value}")


if __name__ == "__main__":
    typer.run(main)
