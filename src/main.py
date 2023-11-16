import typer
import work_with_data


def main(date: str):
    work_with_data.delete_data(date)
    work_with_data.rebuild_report()
    print(f"Очищены все поля начиная с {date}")


if __name__ == "__main__":
    typer.run(main)
